# PROJECT OPERATING SYSTEM — Quant Finance Bootcamp

> Paste this at the start of any new AI conversation to maintain full context.
> Last updated: March 29, 2026 (end of Day 6)

---

## WHO I AM

- 7th grader, middle school
- Name: AB
- GitHub: viraajbindra-a11y
- Strong math background: completed Algebra 2 and Geometry
- Started Python on March 23, 2026
- Have access to LinkedIn Learning
- Built a game called Neon Void (with AI help): https://viraajbindra-a11y.github.io/neon-void/

## MY GOAL

I'm doing a 90-day self-taught bootcamp to get into quantitative finance. I want to learn the fundamentals of math/statistics, Python programming, and finance thinking. I'm not trying to become an expert — I'm trying to get as far as I can and build a strong foundation. No specific end goal like competitions, just learning.

## MY SETUP

- Computer: Mac M1 Air (username: parul@WorkHorse)
- Python version: 3.14.3
- Editor: Thonny (beginner-friendly Python IDE)
- Terminal command: `python3` (not `python` — Mac-specific)
- GitHub Pages site: https://viraajbindra-a11y.github.io/quant-bootcamp/
- Progress tracker (live): https://viraajbindra-a11y.github.io/quant-bootcamp/quant-bootcamp-review.html
- Paper trading game: https://viraajbindra-a11y.github.io/quant-bootcamp/stock-game.html
- Real stock trading app: https://viraajbindra-a11y.github.io/quant-bootcamp/trading-app.html

## SCHEDULE & AVAILABILITY

- Currently on spring break (more time available, 2-3 hours/day)
- Normal schedule: 3-5 hours per week
- Prefers shorter focused sessions over long marathons

## HOW I LEARN BEST

- **Step by step.** Walk me through things one piece at a time. Don't dump a wall of info.
- **Explain as we go.** Don't just give code — explain what each line does and why.
- **TEACH, don't just DO.** On Day 6 I said: "your goal was to teach me things not just have me do things and hope I understand." Running code is NOT the same as learning. Always explain concepts in plain English BEFORE showing code.
- **Test me with quizzes.** Multiple choice review questions help me retain material. Use them frequently.
- **Don't go too fast.** Pace over volume. I'd rather deeply understand 3 concepts than skim 10.
- **Keep it real.** Connect everything to quant finance so I know WHY I'm learning it.
- **I'll say "idk how to code"** — but I can figure things out when guided. I wrote the target price calculator independently on Day 1.
- **Don't code apps for me — I want to learn the concepts.** When I need apps/tools built, I'll say "you code it."

## CRITICAL TEACHING NOTE

On Day 6, I gave critical feedback that the bootcamp was moving too fast. I was running code without understanding what each line did. I couldn't remember material from previous days. The response was to:
1. STOP all new material immediately
2. Switch to plain English concept review
3. Test with quiz questions to find gaps
4. Re-teach weak areas before moving forward

**Always check understanding before introducing new concepts. If I can't explain a concept back, I haven't learned it.**

## CURRENT PROGRESS — DAY 6 COMPLETE, STARTING DAY 7

### Phase 1: Foundations (Spring Break Bootcamp, Days 1–14)

**Day 1 — COMPLETE (3 hours)**
What I learned: print(), input(), float(), variables, math operators (+, -, *, /, **), if/elif/else, str(), round()
Programs built (7 total): hello world, daily return calculator, user input greeter, compound interest calculator, trade analyzer, risk classifier, target price calculator (INDEPENDENT)

**Day 2 — COMPLETE (1.5 hours)**
What I learned: Lists, indexing [0], append(), len(), sum(), max(), min(), for loops, range()
Programs built (3): list operations, three loop patterns, daily return calculator with range()

**Day 3 — COMPLETE (1 hour)**
What I learned: def, parameters, return, calling functions, composing functions together
Functions built: calculate_return(), average(), daily_returns()

**Day 4 — COMPLETE (1.5 hours)**
What I learned: import random, random.choice(), random.random(), nested loops, simulation, Law of Large Numbers
Programs built (4): probability streaks, coin flip simulator, single Monte Carlo sim, full 10,000-simulation Monte Carlo with VaR
Key discovery: Volatility drag — with 50/50 odds and 5% moves, win rate drops to 32.83%

**Day 5 — COMPLETE (2 hours)**
What I learned: Mean (sum/len), variance, standard deviation, Sharpe ratio, bell curve, diversification
Programs built (6): mean calculator, variance/std dev step-by-step, stock comparison with Sharpe, stock analyzer with random.gauss(), bell curve text histogram, portfolio diversification demo
New Python: list comprehensions `[expr for x in list]`, random.gauss(mean, std), float('inf'), f-strings

**Day 6 — COMPLETE (2.5 hours)**
What I learned: Normal distribution, 68-95-99.7 rule, z-scores, Value at Risk (VaR), cumulative distribution function, theory vs simulation validation
Programs built (4): 68-95-99.7 verifier (100K data points), z-score calculator (including Black Monday), risk report with normal_cdf approximation, theory vs simulation comparison
New Python: import math, math.exp(), Abramowitz & Stegun CDF approximation, large-scale verification
**CRITICAL EVENT:** Gave feedback that pace was too fast. Pivoted to full concept review via Q&A quiz. Tested across 3 rounds. Results below.

### Concept Retention Status (tested Day 6):

| Concept | Status | Notes |
|---------|--------|-------|
| Variables | SOLID | Understood immediately |
| Return formula | SOLID | Got 25% correct on the spot |
| Std dev meaning | SOLID | "How spread out the data is" |
| Sharpe ratio | SOLID | Correctly calculated 1%/1% = 1.0 |
| return vs print | SOLID | Knew the difference |
| For loops | RE-LEARNED | No clue initially, re-taught with "hallway doors" metaphor |
| range(3) = 0,1,2 | SOLID | Got correct after re-learning loops |
| List indexing | NEEDS WORK | Got prices[0] and prices[3] right, but missed names[2] (said Tesla, answer was Google) |
| Law of Large Numbers | NEEDS WORK | Knows "more runs = better" but initially thought small sim-theory gap means "math is wrong" |

**KEY RULE: Index 0 = 1st item. Always add 1 to index to get position.**

### Upcoming in Phase 1 (Days 7-14):
- Day 7: Moving Averages & Trend Analysis (NEXT)
- Day 8: Correlation & Portfolio Theory
- Day 9: Real Stock Data (CSV files + pandas intro)
- Day 10: Data Visualization (matplotlib)
- Day 11-14: Projects, review, Phase 2 planning

### Phase 2 (Days 31-60): pandas, matplotlib, correlation, portfolio theory
### Phase 3 (Days 61-90): Moving averages, backtesting, Sharpe ratio, capstone project

## ERRORS I'VE HIT AND RESOLVED

| Error | Cause | Fix | Day |
|-------|-------|-----|-----|
| Couldn't find PATH checkbox | Windows-only, I'm on Mac | Not needed on Mac | 1 |
| `zsh: unknown file attribute: H` | Typed Python code in Terminal instead of Thonny | Use Thonny for Python, Terminal is a different language | 1 |
| $1.47×10²⁰ result | Entered interest rate as 8 instead of 0.08 | Rates must be decimals: 7% = 0.07 | 1 |
| Mental math said 0.2, Python said 0.5 | Wrong mental division: (75-50)/50 = 25/50 = 0.5 | Walk through formula step by step | 3 |
| `SyntaxError: 'return' outside function` | return line wasn't indented inside function | Indent to match other lines in the function body | 3 |
| Ran day5.py instead of day6.py | Created new file but ran old one | Always check you're running the right file in Thonny | 6 |
| Pace too fast, not retaining material | Running code without understanding each line | Pause, review concepts, test with quizzes before moving on | 6 |

## KEY CONCEPTS I UNDERSTAND

- **Return** = (sell - buy) / buy — always divide by buy price
- **Returns stored as decimals** (0.15 = 15%) because math is cleaner for compounding
- **Law of Large Numbers** — more trials = closer to true probability. Small sim-theory differences PROVE the math works.
- **Monte Carlo simulation** — run thousands of random futures to estimate outcomes
- **Value at Risk (VaR)** — worst expected loss at a confidence level (e.g., 95%)
- **Volatility drag** — big % moves hurt you even with fair odds
- **Small edge + many trades > big bets** — 55% daily edge gave 93% yearly win rate
- **Compound interest** = P(1 + r/n)^(nt) — exponential growth
- **Standard deviation** = how spread out data is = measure of risk
- **Sharpe ratio** = mean return / std dev = reward per unit of risk. Higher is better.
- **68-95-99.7 rule** — within 1/2/3 std devs of the mean
- **Z-score** = (value - mean) / std — how many std devs from normal
- **Fat tails** — extreme events happen more than the bell curve predicts (Black Monday z = -11.35)
- **Python counts from 0** — prices[0] is the first item. Index 2 = 3rd item.
- **Indentation matters** — it defines code structure
- **range(a, b) excludes b** — range(1, 5) gives 1, 2, 3, 4. range(3) gives 0, 1, 2.
- **return ≠ print()** — return sends data back silently, print shows on screen
- **Functions are reusable blocks** — write once, call forever, snap together like legos

## FINANCE FORMULAS I KNOW

- Return: `(sell - buy) / buy`
- Compound interest: `p * (1 + r/n) ** (n*t)`
- Average/Mean: `sum(list) / len(list)`
- Daily return: `(prices[i] - prices[i-1]) / prices[i-1]`
- Target price: `price * (1 + gain/100)`
- Variance: `sum([(r - mean)**2 for r in returns]) / len(returns)`
- Standard deviation: `variance ** 0.5`
- Sharpe ratio: `mean / std_dev`
- Z-score: `(return - mean) / std_dev`
- Value at Risk (95%): `mean - 1.645 * std_dev`

## PYTHON I CAN WRITE

```python
# Core skills:
print(), input(), float(), str(), round()
variables, math operators (+, -, *, /, **)
if / elif / else
lists, [indexing], .append(), .sort()
len(), sum(), max(), min()
for loops, range()
def, parameters, return
import random, random.choice(), random.random(), random.gauss()
import math, math.exp()
nested loops (loop inside a loop)
// (integer division)
list comprehensions: [x**2 for x in list]
f-strings: f"Value: {round(x*100, 2)}%"
float('inf')

# Functions I've built:
def calculate_return(buy, sell):
    return (sell - buy) / buy

def average(numbers):
    return sum(numbers) / len(numbers)

def daily_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        r = (prices[i] - prices[i - 1]) / prices[i - 1]
        returns.append(r)
    return returns

def z_score(value, mean, std):
    return (value - mean) / std

def normal_cdf(z):  # Abramowitz and Stegun approximation
    if z < -8: return 0.0
    if z > 8: return 1.0
    t = 1 / (1 + 0.2316419 * abs(z))
    d = 0.3989422804 * math.exp(-z * z / 2)
    p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))))
    if z > 0: return 1 - p
    return p
```

## WHAT I HAVEN'T LEARNED YET

- Dictionaries
- While loops
- File I/O (reading CSV files)
- Libraries (matplotlib, pandas, statistics, csv)
- Moving averages
- Correlation, portfolio theory
- Any real market data analysis (code-based)
- Backtesting strategies

## APPS & TOOLS BUILT FOR ME

1. **VOID MARKET** (stock-game.html) — Paper trading game with 20 simulated stocks, 7 sectors, 4 difficulty modes, training mode, achievements, leaderboard, market indicators, earnings events, auto-trade bot, sound effects
2. **VOID TERMINAL** (trading-app.html) — Real paper trading with Yahoo Finance live data, moving average overlay, news sentiment, portfolio charts, keyboard shortcuts, CSV export, dark/light theme
3. **Progress Website** (quant-bootcamp-review.html) — Full Days 1-6 documentation with code, output, explanations, 15-question quiz, skills tracker, 90-day roadmap, cheat sheet

---

> **Instructions for the AI:** Pick up where I left off. I'm starting Day 7 (Moving Averages & Trend Analysis). IMPORTANT: Teach me, don't just have me run code. Explain concepts in plain English BEFORE showing code. Test me with quizzes regularly. If I can't explain a concept back, I haven't learned it. Check my understanding of list indexing (index 2 = 3rd item) and Law of Large Numbers (small sim-theory gap = math works) before building on them. Walk me through things step by step. Connect everything to quant finance.
