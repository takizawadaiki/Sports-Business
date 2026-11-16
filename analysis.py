"""How four North American leagues pay their players: caps, top contracts, revenue and balance.

    python analysis.py        # reads data/, writes results/results.json
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAPPED = ('NBA', 'NFL', 'NHL')


def read(name):
    with open(HERE / 'data' / name, newline='') as f:
        return list(csv.DictReader(f))


def num(v):
    return float(v) if v not in ('', None) else None


def growth(series, first, last):
    """Fractional change between two seasons of a {season: value} series."""
    return series[last] / series[first] - 1


def share_of_cap(amount, cap):
    return amount / cap


def per_roster_spot(cap, roster):
    return cap / roster


def cap_to_revenue(cap_m, revenue_b, teams):
    """The cap as a share of the average team's revenue."""
    return cap_m / (revenue_b * 1000 / teams)


def main():
    caps = [{k: num(v) for k, v in r.items()} for r in read('caps.csv')]
    series = {lg: {int(r['season']): r[lg.lower()] for r in caps} for lg in CAPPED}
    leagues = {r['league']: {k: (num(v) if k not in ('league', 'system', 'share_of', 'revenue_season', 'max_rule') else v) for k, v in r.items()} for r in read('leagues.csv')}
    top = {r['league']: dict(player=r['player'], team=r['team'], amount=float(r['amount_m']), basis=r['basis']) for r in read('top_contracts.csv')}
    base, current, last = 2015, 2025, int(caps[-1]['season'])
    out = dict(base=base, current=current, last=last, caps=series, nhl_floor={int(r['season']): r['nhl_floor'] for r in caps}, leagues=leagues, top=top, order=['NBA', 'NFL', 'NHL', 'MLB'])
    out['growth'] = {lg: round(growth(series[lg], base, current), 4) for lg in CAPPED}
    out['next_growth'] = {lg: round(growth(series[lg], current, last), 4) for lg in CAPPED}
    out['index'] = {lg: {y: round(v / series[lg][base] * 100, 1) for y, v in series[lg].items()} for lg in CAPPED}
    for lg, L in leagues.items():
        line = L['cap_m'] or L['tax_line_m']                       # MLB has no cap, so its top contract is set against the tax threshold
        L['line_m'] = line
        L['top_share'] = round(share_of_cap(top[lg]['amount'], line), 4)
        L['per_roster_spot_m'] = round(per_roster_spot(line, L['roster']), 3)
        L['avg_team_revenue_m'] = round(L['revenue_b'] * 1000 / L['teams'], 1)
        L['line_to_revenue'] = round(cap_to_revenue(line, L['revenue_b'], L['teams']), 4)
        L['floor_share'] = round(L['floor_m'] / L['cap_m'], 4) if L['floor_m'] and L['cap_m'] else None
        L['max_share'] = round(L['max_salary_m'] / L['cap_m'], 4) if L['max_salary_m'] and L['cap_m'] else None
    out['balance'] = {r['league']: dict(noll_scully=float(r['noll_scully']), next_season_r=float(r['next_season_r']), seasons=r['seasons']) for r in read('balance.csv')}
    (HERE / 'results').mkdir(exist_ok=True)
    (HERE / 'results' / 'results.json').write_text(json.dumps(out, separators=(',', ':')) + '\n')
    for lg, L in leagues.items():
        print(lg, {k: L[k] for k in ('line_m', 'top_share', 'per_roster_spot_m', 'avg_team_revenue_m', 'line_to_revenue', 'floor_share', 'max_share')})
    print(out['growth'], out['next_growth'])


if __name__ == '__main__':
    main()
