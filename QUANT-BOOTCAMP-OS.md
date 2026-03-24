# PROJECT OPERATING SYSTEM — Quant Finance Bootcamp

> Paste this at the start of any new AI conversation to maintain full context.
> Last updated: March 24, 2026 (end of Day 4)

---

## WHO I AM

- 7th grader, middle school
- Name: AB
- GitHub: viraajbindra-a11y
- Strong math background: completed Algebra 2 and Geometry
- Brand new to Python (started March 23, 2026)
- Brand new to finance concepts
- Have access to LinkedIn Learning
- Built a game called Neon Void (with AI help): https://viraajbindra-a11y.github.io/neon-void/

## MY GOAL

I'm doing a 90-day self-taught bootcamp to get into quantitative finance. I want to learn the fundamentals of math/statistics, Python programming, and finance thinking. I'm not trying to become an expert — I'm trying to get as far as I can and build a strong foundation. No specific end goal like competitions, just learning.

## MY SETUP

- Computer: Mac (username: parul@WorkHorse)
- Python version: 3.14.3
- Editor: Thonny (beginner-friendly Python IDE)
- Terminal command: `python3` (not `python` — Mac-specific)
- GitHub Pages site: https://viraajbindra-a11y.github.io/quant-bootcamp/
- Progress tracker (live): https://viraajbindra-a11y.github.io/quant-bootcamp/quant-bootcamp-review.html

## SCHEDULE & AVAILABILITY

- Currently on spring break (more time available, 2-3 hours/day)
- Normal schedule: 3-5 hours per week
- Prefers shorter focused sessions over long marathons

## HOW I LEARN BEST

- **Step by step.** Walk me through things one piece at a time. Don't dump a wall of info.
- **Explain as we go.** Don't just give code — explain what each line does and why.
- **Let me try first.** Give me skeletons/hints before full solutions. But if I'm stuck, just give me the answer and explain it.
- **Don't go too fast.** I once said "this is going fast, how will this be 2 hours?" — pace matters.
- **Keep it real.** Connect everything to quant finance so I know WHY I'm learning it.
- **I'll say "idk how to code"** — but I can actually figure things out when guided. I wrote Program 6 (target price calculator) independently on Day 1 after saying that.

## CURRENT PROGRESS — DAY 4 COMPLETE, STARTING DAY 5

### Phase 1: Foundations (Spring Break Bootcamp, Days 1–14)

**Day 1 — COMPLETE (3 hours)**
What I learned: print(), input(), float(), variables, math operators (+, -, *, /, **), if/elif/else, str(), round()
Programs built (6 total):
1. Hello world
2. Daily return calculator (variables and math)
3. User input greeter
4. Compound interest calculator: `a = p * (1 + r/n) ** (n*t)`
5. Trade analyzer (if/elif/else — profit, break even, or loss)
6. Risk classifier (std_dev thresholds)
7. Target price calculator (WRITTEN INDEPENDENTLY — milestone)

**Day 2 — COMPLETE (1.5 hours)**
What I learned: Lists, indexing [0], append(), len(), sum(), max(), min(), for loops, range()
Programs built:
1. List operations (creating, accessing, built-in functions)
2. Three loop patterns (print each, conditional check, counting)
3. Daily return calculator across a list of prices using range() and indexing

**Day 3 — COMPLETE (1 hour)**
What I learned: def, parameters, return, calling functions, composing functions together
Functions built:
- `calculate_return(buy, sell)` — computes (sell - buy) / buy
- `average(numbers)` — computes sum/len
- `daily_returns(prices)` — loops through prices, calculates return between consecutive days, returns list
Milestone: Combined functions together (daily_returns output fed into average)

**Day 4 — COMPLETE (1.5 hours)**
What I learned: import random, random.choice(), random.random(), nested loops, simulation, Law of Large Numbers
Programs built:
1. Probability of streaks calculator (0.6⁵ = 7.78%)
2. Coin flip simulator (1,000 and 100,000 flips — demonstrated Law of Large Numbers)
3. Single Monte Carlo stock simulation (one random future over 252 days)
4. Full Monte Carlo with 10,000 simulations + risk analysis (best/worst/average/median/VaR)
Key experiments: Ran 4 comparisons of edge size (50% vs 55%) and move size (1% vs 5%)
Key discovery: Volatility drag — with 50/50 odds and 5% moves, win rate drops to 32.83% because losses are harder to recover from than gains
Finance concepts: Monte Carlo simulation, Value at Risk (VaR), volatility drag, Law of Large Numbers, "small edge repeated many times beats big volatile bets"

**Day 5 — NOT STARTED**
Planned: Statistics (mean, variance, standard deviation) calculated by hand and in code

### Upcoming in Phase 1 (Days 5-14):
- Day 5: Statistics (mean, variance, standard deviation)
- Day 6: Expected value
- Day 7: Rest/catch-up
- Day 8: Statistics (mean, variance, standard deviation)
- Day 9: Real stock data (CSV files from Yahoo Finance)
- Day 10: Data visualization (matplotlib)
- Day 11: Expected value
- Day 12: Normal distribution (bell curve)
- Day 13: Multi-stock analysis project
- Day 14: Review and plan Phase 2

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

## KEY CONCEPTS I UNDERSTAND

- **Return** = (sell - buy) / buy — always divide by buy price
- **Returns stored as decimals** (0.15 = 15%) because math is cleaner for compounding
- **Law of Large Numbers** — more trials = closer to true probability (100k coin flips → 49.876%)
- **Monte Carlo simulation** — run thousands of random futures to estimate outcomes
- **Value at Risk (VaR)** — worst 1% outcome measures downside risk
- **Volatility drag** — big % moves hurt you even with fair odds because losses are harder to recover from
- **Small edge + many trades > big bets** — 55% daily edge gave 93% yearly win rate with 1% moves
- **Compound interest** = P(1 + r/n)^(nt) — exponential growth
- **Standard deviation** = measure of risk/volatility
- **Python counts from 0** — prices[0] is the first item
- **Indentation matters** — it's not cosmetic, it defines code structure
- **range(a, b) excludes b** — range(1, 5) gives 1, 2, 3, 4
- **return ≠ print()** — return sends data back silently, print shows on screen
- **Functions are reusable blocks** — write once, call forever, snap together like legos

## FINANCE FORMULAS I KNOW

- Return: `(sell - buy) / buy`
- Compound interest: `p * (1 + r/n) ** (n*t)`
- Average: `sum(list) / len(list)`
- Daily return: `(prices[i] - prices[i-1]) / prices[i-1]`
- Target price: `price * (1 + gain/100)`

## PYTHON I CAN WRITE

```python
# I can use all of these:
print(), input(), float(), str(), round()
variables, math operators (+, -, *, /, **)
if / elif / else
lists, [indexing], .append(), .sort()
len(), sum(), max(), min()
for loops, range()
def, parameters, return
import random, random.choice(), random.random()
nested loops (loop inside a loop)
// (integer division)

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
```

## WHAT I HAVEN'T LEARNED YET

- Dictionaries
- While loops
- File I/O (reading CSV files)
- Libraries (matplotlib, pandas, statistics, csv)
- Standard deviation, variance (calculating in code)
- Any real market data analysis
- Expected value, normal distribution
- Correlation, portfolio theory

---

> **Instructions for the AI:** Pick up where I left off. I'm starting Day 5 (Statistics: mean, variance, standard deviation). Walk me through things step by step. Don't go too fast. Explain concepts as we go. Connect everything to quant finance. If I say "idk" or seem stuck, give hints first, then the full answer if needed. Keep sessions focused and paced — I'll tell you how much time I have.
