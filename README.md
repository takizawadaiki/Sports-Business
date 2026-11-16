# How four leagues pay their players

Live page: https://takizawadaiki.github.io/Sports-Business/

The NBA, NFL, NHL and MLB side by side: the cap rules, how fast the caps have grown, how much one star can take, league revenue, and whether caps go with more even standings.

## Findings

- The three capped leagues give players about half of shared revenue (NBA 49 to 51%, NFL 48 to 48.5%, NHL 50%). MLB has no cap and no fixed share.
- From 2015 to 2025 the NBA cap grew 121%, the NFL cap 95% and the NHL cap 34%.
- The top NBA salary (Stephen Curry, $59.6 million) is 38.5% of the cap. The top NFL contract is 21.5% and the top NHL cap hit 14.7%.
- Divided by roster size, the NBA cap is $10.3 million a player, the NFL's $5.3 million and the NHL's $4.2 million.
- The NBA has the least even standings of the four (Noll-Scully 2.68), less even than MLB (1.86) with no cap. The NHL (1.62) and NFL (1.54) are the most even.

## Files

| Path | What it is |
| --- | --- |
| `data/` | Caps by season, the 2025-26 rules and revenue for each league, top contracts and balance measures, with `SOURCES.md` |
| `analysis.py` | Growth, shares of the cap, cap per roster spot; writes `results/results.json` |
| `tests/test_analysis.py` | Five tests |
| `index.html` | The page |

## Limits

League revenue figures are Forbes estimates and are broader than the revenue each agreement shares with players. A cap is not a payroll: NBA teams can exceed theirs. Top contracts are measured as salary or cap hit in the NBA and NHL and as a yearly average in the NFL.

An earlier version of this page included team payrolls, efficiency scores and inequality measures that could not be traced to reliable sources. They have been removed.

```
python analysis.py
python -m pytest tests
```
