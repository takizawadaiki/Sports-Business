import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import analysis as A


def test_growth_is_the_change_between_two_seasons():
    assert abs(A.growth({2015: 70.0, 2025: 154.647}, 2015, 2025) - 1.2092) < 1e-3


def test_share_of_cap_and_roster_spot():
    assert abs(A.share_of_cap(14.0, 95.5) - 0.1466) < 1e-4
    assert abs(A.per_roster_spot(279.2, 53) - 5.268) < 1e-3


def test_cap_to_revenue_uses_the_average_team():
    assert abs(A.cap_to_revenue(100.0, 6.4, 32) - 0.5) < 1e-9       # $6.4B over 32 teams is $200M a team


def test_caps_never_fall_except_the_nfl_in_2021():
    A.main()
    R = json.loads((ROOT / 'results' / 'results.json').read_text())
    for lg, s in R['caps'].items():
        years = sorted(s, key=int)
        drops = [y for a, y in zip(years, years[1:]) if s[y] < s[a]]
        assert drops == (['2021'] if lg == 'NFL' else [])


def test_results_put_the_nba_star_above_the_league_maximum_and_the_nhl_star_below():
    R = json.loads((ROOT / 'results' / 'results.json').read_text())
    L = R['leagues']
    assert L['NBA']['top_share'] > L['NBA']['max_share'] and L['NHL']['top_share'] < L['NHL']['max_share']
    assert L['MLB']['cap_m'] is None and L['MLB']['line_m'] == 241
