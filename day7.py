# ============================================
# DAY 7 — MOVING AVERAGES & TREND ANALYSIS
# ============================================
# Today we learn one of the most important tools in ALL of trading.
# Every hedge fund, every quant, every trader uses moving averages.
#
# WHAT IS A MOVING AVERAGE?
# Stock prices jump around day to day — noisy and chaotic.
# A moving average SMOOTHS it out by averaging the last N days.
# Instead of "what's the price today?" you ask "what's the TREND?"
#
# Think of it like this:
# Your weight bounces around daily (water, food, etc.)
# But if you average each WEEK, you see the real trend.
# Moving averages do the same thing for stock prices.

import random

# ============================================
# PART 1: YOUR FIRST MOVING AVERAGE
# ============================================
# Let's calculate a 5-day moving average by hand.
# For each day, we average THAT day and the 4 days before it.
# So we need at least 5 days of data before we can start.

print("=" * 50)
print("PART 1: 5-Day Moving Average")
print("=" * 50)

prices = [100, 102, 98, 103, 107, 104, 110, 108, 112, 115, 111, 116, 120, 118, 122]

# Let's walk through the first moving average calculation:
# Day 5 (index 4): average of prices[0] through prices[4]
# That's: (100 + 102 + 98 + 103 + 107) / 5

window = 5  # "window" means how many days we look back

print(f"\nStock prices: {prices}")
print(f"Window size: {window} days")
print()

# Calculate moving averages
moving_averages = []

for i in range(window - 1, len(prices)):
    # Get the last 'window' prices ending at position i
    chunk = prices[i - window + 1 : i + 1]
    avg = sum(chunk) / len(chunk)
    moving_averages.append(round(avg, 2))

    # Show the work for the first 3
    if i < window + 2:
        print(f"Day {i+1}: prices {chunk} → average = {avg:.2f}")

print(f"\nAll moving averages: {moving_averages}")
print(f"Original prices had {len(prices)} points")
print(f"Moving averages has {len(moving_averages)} points")
print(f"(We lose the first {window-1} days because we need {window} days of history)")

# ============================================
# PART 2: WHY MOVING AVERAGES MATTER
# ============================================
# Here's the KEY insight: when the price crosses ABOVE the moving average,
# that's a BUY signal. When it drops BELOW, that's a SELL signal.
# This is called a "crossover strategy."

print("\n" + "=" * 50)
print("PART 2: Buy & Sell Signals")
print("=" * 50)

# Compare each price to its moving average
print(f"\n{'Day':<6} {'Price':<10} {'5-Day MA':<12} {'Signal':<10}")
print("-" * 38)

for i in range(len(moving_averages)):
    day = i + window - 1  # moving averages start at day 5 (index 4)
    price = prices[day]
    ma = moving_averages[i]

    if price > ma:
        signal = "ABOVE ↑"
    elif price < ma:
        signal = "BELOW ↓"
    else:
        signal = "EQUAL"

    print(f"{day+1:<6} ${price:<9} ${ma:<11} {signal}")

# ============================================
# PART 3: BUILD A MOVING AVERAGE FUNCTION
# ============================================
# Let's make this reusable!

print("\n" + "=" * 50)
print("PART 3: Moving Average Function")
print("=" * 50)

def moving_average(prices, window):
    """Calculate the moving average for a list of prices.

    prices: list of numbers
    window: how many days to look back
    Returns: list of moving averages (shorter than original by window-1)
    """
    mas = []
    for i in range(window - 1, len(prices)):
        chunk = prices[i - window + 1 : i + 1]
        mas.append(sum(chunk) / len(chunk))
    return mas

# Test with different windows
ma_5 = moving_average(prices, 5)
ma_3 = moving_average(prices, 3)
ma_10 = moving_average(prices, 10)

print(f"5-day MA:  {[round(x,1) for x in ma_5]}")
print(f"3-day MA:  {[round(x,1) for x in ma_3]}")
print(f"10-day MA: {[round(x,1) for x in ma_10]}")
print()
print("Notice: shorter window (3) = more wiggly, reacts faster")
print("        longer window (10) = smoother, reacts slower")
print("Quants pick the window based on their trading style:")
print("  Short-term traders: 5-20 day MA")
print("  Long-term investors: 50-200 day MA")
print("  The famous '200-day moving average' is watched by EVERYONE on Wall Street")

# ============================================
# PART 4: SIMULATED TRADING STRATEGY
# ============================================
# Let's test if moving averages actually WORK as a strategy!
# We'll generate a random stock and see if the MA strategy makes money.

print("\n" + "=" * 50)
print("PART 4: Does the Strategy Actually Work?")
print("=" * 50)

# Generate 252 days (one year) of a stock with a slight upward trend
random.seed(42)  # Same result every time for comparison
start_price = 100
daily_drift = 0.0003  # Slight upward bias
daily_vol = 0.02      # 2% daily volatility

stock_prices = [start_price]
for day in range(251):
    change = random.gauss(daily_drift, daily_vol)
    new_price = stock_prices[-1] * (1 + change)
    stock_prices.append(round(new_price, 2))

print(f"Generated {len(stock_prices)} days of stock data")
print(f"Start price: ${stock_prices[0]}")
print(f"End price: ${stock_prices[-1]}")
print(f"Buy-and-hold return: {round((stock_prices[-1]/stock_prices[0] - 1) * 100, 2)}%")

# Now test the MA crossover strategy
window_size = 20  # 20-day moving average
ma = moving_average(stock_prices, window_size)

cash = 10000
shares = 0
buy_price = 0
trades = 0
wins = 0
losses = 0

# Start trading after we have enough data for the MA
for i in range(1, len(ma)):
    day = i + window_size - 1
    price = stock_prices[day]
    prev_price = stock_prices[day - 1]

    # Buy signal: price crosses ABOVE the MA
    if price > ma[i] and prev_price <= ma[i-1] and shares == 0:
        shares = cash / price
        buy_price = price
        cash = 0
        trades += 1

    # Sell signal: price crosses BELOW the MA
    elif price < ma[i] and prev_price >= ma[i-1] and shares > 0:
        cash = shares * price
        if price > buy_price:
            wins += 1
        else:
            losses += 1
        shares = 0
        trades += 1

# If still holding at the end, sell
if shares > 0:
    cash = shares * stock_prices[-1]
    if stock_prices[-1] > buy_price:
        wins += 1
    else:
        losses += 1
    trades += 1

ma_return = (cash / 10000 - 1) * 100
bah_return = (stock_prices[-1] / stock_prices[0] - 1) * 100

print(f"\n--- STRATEGY RESULTS ---")
print(f"Starting cash: $10,000")
print(f"Final cash (MA strategy): ${cash:,.2f}")
print(f"MA strategy return: {ma_return:.2f}%")
print(f"Buy-and-hold return: {bah_return:.2f}%")
print(f"Total trades: {trades}")
print(f"Winning trades: {wins}")
print(f"Losing trades: {losses}")
if wins + losses > 0:
    print(f"Win rate: {wins/(wins+losses)*100:.0f}%")

if ma_return > bah_return:
    print("\nMA strategy BEAT buy-and-hold!")
else:
    print("\nBuy-and-hold won this time.")
    print("(MA strategies don't always win — they're best in TRENDING markets)")

# ============================================
# PART 5: COMPARING WINDOW SIZES
# ============================================
# Which window size works best? Let's test several!

print("\n" + "=" * 50)
print("PART 5: Window Size Comparison")
print("=" * 50)

def test_strategy(prices, window_size):
    """Test a moving average crossover strategy and return the final return %."""
    ma = moving_average(prices, window_size)
    cash = 10000
    shares = 0
    buy_p = 0

    for i in range(1, len(ma)):
        day = i + window_size - 1
        price = prices[day]
        prev = prices[day - 1]

        if price > ma[i] and prev <= ma[i-1] and shares == 0:
            shares = cash / price
            buy_p = price
            cash = 0
        elif price < ma[i] and prev >= ma[i-1] and shares > 0:
            cash = shares * price
            shares = 0

    if shares > 0:
        cash = shares * prices[-1]

    return round((cash / 10000 - 1) * 100, 2)

print(f"\n{'Window':<10} {'Return':<12} {'vs Buy&Hold':<15}")
print("-" * 37)

bah = round((stock_prices[-1] / stock_prices[0] - 1) * 100, 2)

for w in [5, 10, 20, 50, 100]:
    ret = test_strategy(stock_prices, w)
    diff = round(ret - bah, 2)
    marker = "BEAT" if diff > 0 else "LOST"
    print(f"{w}-day    {ret}%       {'+' if diff > 0 else ''}{diff}% ({marker})")

print(f"\nBuy & Hold: {bah}%")
print("\nKey insight: There's no 'best' window size that works every time.")
print("Short windows catch trends early but get faked out by noise.")
print("Long windows miss the start of trends but avoid false signals.")
print("This tradeoff is at the HEART of quantitative trading.")
