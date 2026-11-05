#!/usr/bin/env python3
"""Score the frozen Athanor n=10 forecast without refitting or overwriting it.

Usage: python3 -I score_forecast.py profile-n10.json predictions-n10.json
The scoring rule was frozen in predictions-n10.md before these exact counts existed.
"""
import json
import math
import sys


def score_cell(y, p, lower, upper):
    assert lower <= p <= upper
    interval = (upper - lower) + 10 * max(lower - y, 0) + 10 * max(y - upper, 0)
    return ((0.5 * abs(y - p) + 0.1 * interval) / 1.5,
            abs(y - p), lower <= y <= upper, interval)


def summarize(cells):
    n = len(cells)
    return {'n': n, 'mean_wis': sum(c[0] for c in cells) / n,
            'mae': sum(c[1] for c in cells) / n,
            'coverage80': sum(c[2] for c in cells), 'outside80': n - sum(c[2] for c in cells)}


def main(actual_path, frozen_path):
    a = json.load(open(actual_path))
    frozen = json.load(open(frozen_path))
    assert a['n'] == 10 and a['status'] == 'exact (two programs agree)'
    rules = frozen['scoring']
    assert rules['count_targets'] == list(range(12, 20))
    assert rules['maximal_targets'] == list(range(14, 20))
    assert rules['known_endpoint_excluded'] == 20
    result = {'actual_peak': max(range(len(a['profile'])), key=lambda k: a['profile'][k]),
              'actual_first_extendable_fraction_below_half': next(
                  k for k, (total, maximal) in enumerate(zip(a['profile'], a['maximal_profile']))
                  if total and 2 * maximal > total),
              'models': {}}
    for model in frozen['models']:
        counts = {v['m']: v for v in model['ln_a']}
        maximal = {v['m']: v for v in model['maximal_counts']}
        count_cells = [score_cell(math.log(a['profile'][k]), counts[k]['point'],
                                  counts[k]['lower80'], counts[k]['upper80'])
                       for k in rules['count_targets']]
        max_cells = [score_cell(math.log1p(a['maximal_profile'][k]),
                                math.log1p(maximal[k]['point']),
                                math.log1p(maximal[k]['lower80']),
                                math.log1p(maximal[k]['upper80']))
                     for k in rules['maximal_targets']]
        cs, ms = summarize(count_cells), summarize(max_cells)
        secondary = {}
        for label, actual, key in (
            ('peak', result['actual_peak'], 'peak_position'),
            ('first_below_half', result['actual_first_extendable_fraction_below_half'],
             'first_extendable_fraction_below_half'),
        ):
            forecast = model[key]
            _, error, covered, interval_score = score_cell(
                actual, forecast['point'], forecast['lower80'], forecast['upper80'])
            secondary[label] = {'actual': actual, 'point': forecast['point'],
                                'lower80': forecast['lower80'], 'upper80': forecast['upper80'],
                                'absolute_error': error, 'IS80': interval_score,
                                'coverage80': covered}
        result['models'][model['id']] = {
            'primary_wis': 0.5 * cs['mean_wis'] + 0.5 * ms['mean_wis'],
            'ln_counts': cs, 'ln1p_maximal': ms,
            'secondary': secondary,
            'topology_status': 'not scored; requires a completion-support graph census'}
    assert set(result['models']) == {'Q', 'H'}
    q, h = (result['models'][s]['primary_wis'] for s in ('Q', 'H'))
    result['winner_under_frozen_0_01_gate'] = ('tie' if abs(q-h) < 0.01 else
                                             ('Q' if q < h else 'H'))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: score_forecast.py profile-n10.json predictions-n10.json')
    main(sys.argv[1], sys.argv[2])
