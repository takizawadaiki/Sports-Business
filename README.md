# Sports Business Intelligence Dashboard · 2025-26 Season
### NBA · NHL · NFL · MLB — Salary Cap Economics, Revenue & Competitive Balance

> **Live demo:** [your-username.github.io/sports-bi](https://your-username.github.io/sports-bi)  
> **Stack:** HTML · CSS · JavaScript · Chart.js · PapaParse · No backend required  
> **Data:** Verified 2025-26 official cap figures · Sportico/Forbes revenue estimates · Spotrac/ESPN contracts

---

## Overview

A self-contained sports economics analytics dashboard comparing the business structures of four major North American professional sports leagues — the NBA, NHL, NFL, and MLB. Built to answer questions at the intersection of labor economics, competitive strategy, and sports business intelligence:

- How do salary cap systems differ in structure and enforcement?
- Is the NHL cap low relative to league revenue — and by how much?
- What share of league revenue flows to players?
- How concentrated are salaries at the top of each roster?
- Which league achieves the most genuine competitive parity?
- Does higher payroll predict playoff success differently across leagues?
- **What happens with no salary cap at all? — MLB's uncapped economy vs the capped leagues**
- How does roster size distort per-player economics?

Fully interactive, dark-mode first, structured as a portfolio-grade analytics deliverable.

---

## Key Analytical Findings

### Finding 1 — NBA: Steph Curry's 38.6% cap share is a historical record
At $59,606,817 on a $154.647M cap, Curry consumes a larger share of his league's cap than any player in any major pro sport. For context, the entire NHL's highest-paid player (Draisaitl) earns $14M — less than a quarter of Curry's salary — and counts for 14.7% of the NHL cap.

### Finding 2 — NHL: The cap is finally catching up — $95.5M → $113.5M by 2027-28
After years of near-flat caps following COVID escrow repayments, the NHL announced a confirmed three-year roadmap. The league posted record revenue of $7B+ in 2024-25. Kirill Kaprizov's $17M/yr deal (starting 2026-27) will be the richest in NHL history — but still less than Curry earns this season.

### Finding 3 — NFL: The cap crossed $300M for the first time in 2026
The 2025 NFL cap hit $279.2M (+$23.8M), and the 2026 cap is confirmed at $301.2M — the first time it has cleared $300M. Quarterback economics dominate: Dak Prescott's $60M AAV leads, followed by four QBs at $55M. The top 16 highest-paid NFL players are all quarterbacks.

### Finding 4 — NBA: OKC Thunder won the title on a below-market payroll
The Thunder's 2024-25 championship (68-14 regular season) came while SGA earned $38.3M — well below what his elite peers make — because his supermax extension doesn't kick in until 2027-28. The "rookie contract window" efficiency premium is the NBA's primary path to cap-efficient championship contention.

### Finding 5 — NHL: Florida Panthers' back-to-back Cups challenge the "hard cap prevents dynasties" narrative
The Panthers won consecutive Stanley Cups (2024, 2025) through smart long-term extensions on core players before the market corrected upward — not through financial dominance. Dynasty in the NHL is a roster construction problem, not a payroll problem.

### Finding 6 — Cross-league: Revenue per active player gap is 3.0× (NBA vs NHL)
NBA: $14.3B / 450 players = $31.8M per player. NHL: $7.7B / 736 players = $10.5M. NFL: $23B / 1,696 players = $13.6M. MLB: $12.25B / ~750 active players = ~$16.3M. The NBA's new $76B media deal is widening this gap further.

### Finding 7 — MLB: The Dodgers' luxury tax bill exceeds 12 teams' entire payrolls
MLB's cap-free model produces the widest spending gap in pro sports: Mets $342M vs Marlins $87M — a **3.93× ratio**. In capped leagues, that ratio is under 2.0×. The Dodgers paid $169M in luxury tax in 2025 — more than the full payroll of every team in the bottom third of the league. Yet high payroll predicts wins more weakly in MLB than in the NBA: the $342M Mets missed the playoffs entirely.

---

## Dashboard Sections

| Section | What it covers |
|---|---|
| **Key Findings** | Seven original analytical conclusions with supporting data |
| **Overview** | Cap trajectory (2015–2026), indexed growth, top-line metrics |
| **Cap Systems** | CBA structure comparison across NBA, NHL, NFL — max %, cap per spot |
| **Revenue & Labor** | League revenue, player labor share, revenue per active player |
| **Salary Distribution** | Gini coefficients, Lorenz curves, top-N cap share, player scatter |
| **Competitive Parity** | Championship diversity, playoff repeat rates, payroll-parity scatter |
| **Payroll Efficiency** | Wins vs payroll scatter per league, $/win metrics |
| **Team Explorer** | Filter/sort all teams, upload your own CSV, tier distribution |
| **⚾ MLB (No Cap)** | All 30 team payrolls, CBT mechanics, payroll vs wins, four-league spread comparison, largest contracts in pro sports history |

---

## Metrics & Formulas

### Gini Coefficient
```
G = 1 − (2/n) × Σ(i=1→n) [ (n−i+0.5) × s_i / Σs ]
```
Measures salary inequality within rosters. 0 = perfect equality, 1 = maximum inequality. Computed live from the player salary CSV layer using actual 2025-26 contracts.

### Payroll Efficiency ($/Win)
```
Efficiency = Team Active Payroll ($M) / Regular Season Wins
```
Lower = better. Compare within leagues only — NBA/NHL play 82 games, NFL 17, MLB 162.

### Labor Share of Revenue
```
Labor Share = Total League Payroll / Estimated League Revenue × 100
```
Each CBA defines its base differently: BRI (NBA), HRR (NHL), AR (NFL). MLB has no CBA revenue split mechanism — the CBT redistributes tax revenue, not a fixed player percentage.

### Top-N Salary Share
```
Top-N Share = Σ(top N salaries on team) / Total Team Payroll × 100
```
Averaged across all teams per league. Reveals payroll concentration at the top.

### Revenue Per Active Player
```
Rev/Player = League Revenue / (Teams × Active Roster Size)
```
Macro productivity proxy. Driven by league size and roster architecture, not individual performance.

### Payroll Spread Ratio (MLB-specific)
```
Spread Ratio = Highest team payroll / Lowest team payroll
```
MLB 2025: $342M / $87M = **3.93×**. NBA: ~1.75×. NHL: ~1.37×. NFL: ~1.35×.

### Championship Diversity Index
```
CDI(window) = Unique champions in rolling 5-year window / 5
```
Ranges from 0.2 (same team every year) to 1.0 (all different). Higher = more parity.

### Cap Growth Index
```
Index_t = Cap_t / Cap_2015 × 100
```
Normalizes all leagues to a 2015 baseline of 100 for direct growth comparison.

---

## Data Sources · 2025-26

| Dataset | Source | Coverage | Status |
|---|---|---|---|
| NBA cap $154.647M | NBA.com official press release | 2025-26 season | ✅ Verified |
| NHL cap $95.5M | NHL.com / Puckpedia | 2025-26 season | ✅ Verified |
| NFL cap $279.2M | NFL.com / OverTheCap | 2025 season | ✅ Verified |
| NFL 2026 cap $301.2M | NFL Football Operations | 2026 season | ✅ Verified |
| MLB CBT threshold $241M | MLB / Spotrac | 2025 season | ✅ Verified |
| MLB team payrolls | ESPN, USA Today, MLBTR | 2025 final payrolls | ✅ Verified |
| MLB luxury tax bills | AP / ESPN ($403M total) | 2025 season | ✅ Verified |
| Player salaries (NBA) | ESPN.com / Spotrac | 2025-26 active contracts | ✅ Verified |
| Player salaries (NHL) | USA Today / Spotrac | 2025-26 cap hits | ✅ Verified |
| Player salaries (NFL) | Spotrac / Athlon Sports | 2025 AAV | ✅ Verified |
| Player salaries (MLB) | MLB Labor Relations Dept. | 2025 present-day values | ✅ Verified |
| NBA revenue $14.3B | Sportico (Nov 2025) | 2025-26 projected | Estimated |
| NHL revenue $7.7B | Sportico / Statista | 2024-25 actual | Estimated |
| NFL revenue ~$23B | Sportico / Forbes | 2024-25 actual | Estimated |
| MLB revenue ~$12.25B | CNBC / Forbes | 2024-25 actual | Estimated |
| 2025 MLB champion | ESPN / MLB.com | LA Dodgers (WS) | ✅ Verified |
| 2025 NBA champion | NBA.com | OKC Thunder (68-14) | ✅ Verified |
| 2024-25 NHL champion | NHL.com | Florida Panthers (2×) | ✅ Verified |
| Gini / Lorenz curves | Derived from player salary data | Computed client-side | Derived |

---

## Using Your Own Data

The dashboard uses [PapaParse](https://www.papaparse.com/) to parse CSV data client-side. No server required.

### Team payroll CSV format (NBA / NHL / NFL)
```csv
team,payroll,cap,wins,league,status
Boston Celtics,212,154.6,61,NBA,Over Tax
Edmonton Oilers,97,95.5,57,NHL,Over LTIR
Kansas City Chiefs,282,279.2,15,NFL,Over Cap
```

### MLB team CSV format
```csv
team,payroll,wins,tax,division
Los Angeles Dodgers,321,98,169.0,NL West
New York Mets,342,83,97.1,NL East
Miami Marlins,87,62,0,NL East
```

### Player salary CSV format
```csv
name,league,team,position,age,salary_m
Nikola Jokic,NBA,Denver Nuggets,C,30,55.2
Leon Draisaitl,NHL,Edmonton Oilers,C,30,14.0
Juan Soto,MLB,New York Mets,OF,27,61.9
```

Upload via the **Team Explorer → Data Layer** import panel. Data stays in your browser — nothing is sent anywhere.

---

## URL Deep Linking

The dashboard supports URL parameters for deep linking:

```
index.html?tab=mlb                      → MLB (No Cap) tab
index.html?tab=cap                      → Cap Systems tab
index.html?tab=explorer&league=nhl      → Team Explorer, NHL pre-selected
index.html?tab=efficiency&league=nfl    → Efficiency tab, NFL view
index.html?tab=parity                   → Competitive Parity tab
index.html?tab=findings                 → Key Findings (default)
```

Valid `tab` values: `findings`, `overview`, `cap`, `revenue`, `concentration`, `parity`, `efficiency`, `explorer`, `mlb`  
Valid `league` values (explorer/efficiency tabs): `nba`, `nhl`, `nfl`

---

## Project Structure

```
sports-bi/
├── index.html          ← Single-file dashboard (all JS/CSS inline)
├── README.md           ← This file
├── data/               ← (optional) real CSV exports go here
│   ├── nba_teams.csv
│   ├── nhl_teams.csv
│   ├── nfl_teams.csv
│   ├── mlb_teams.csv
│   └── players.csv
└── screenshots/
    ├── key-findings.png
    ├── mlb-no-cap.png
    ├── cap-systems.png
    └── team-explorer.png
```

---

## Deploying to GitHub Pages

```bash
# 1. Create a new repo on GitHub named sports-bi
git init
git add index.html README.md
git commit -m "feat: sports business intelligence dashboard — NBA/NHL/NFL/MLB"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sports-bi.git
git push -u origin main

# 2. Enable GitHub Pages
# Settings → Pages → Source → Deploy from branch → main → / (root) → Save

# 3. Live at:
# https://YOUR_USERNAME.github.io/sports-bi
```

The entire project is a single `index.html` — no build step, no dependencies to install.

---

## Skills Demonstrated

| Skill | Where |
|---|---|
| Data wrangling & CSV parsing | PapaParse data layer, inline CSV structure across 4 leagues |
| Statistical metrics | Gini, Lorenz, percentiles, labor share, spread ratio — computed client-side |
| Data visualization | Chart.js — scatter, bar, line, doughnut, grouped, indexed, annotated |
| Business intelligence | 7 original analytical findings with quantified conclusions |
| Sports economics domain knowledge | CBA structures, CBT mechanics, cap vs no-cap comparison, labor share formulas |
| Cross-league benchmarking | 4-league comparison framework including MLB as uncapped control case |
| Front-end engineering | Responsive dark-mode UI, URL routing, modal system, CSV upload, live Gini computation |
| Portfolio communication | Executive summary, methodology section, data source documentation |

---

## Resume / LinkedIn Summary

> *Sports Business Intelligence Dashboard — Built an interactive 4-league analytics platform (NBA, NHL, NFL, MLB) comparing salary cap structures, revenue economics, payroll efficiency, and competitive balance. Computed Gini coefficients, Lorenz curves, and payroll spread ratios from verified 2025-26 data. Includes MLB as an uncapped control case, with all-time contract comparisons and CBT mechanics analysis. Stack: HTML/JS, Chart.js, PapaParse. Deployed on GitHub Pages.*

---

*Last updated: May 2026 · All cap figures from official 2025-26 league announcements · MLB data from ESPN/AP/Spotrac*
