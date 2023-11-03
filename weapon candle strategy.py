//@version=5
strategy("Weapon Candle Long Strategy", overlay=true)

// Define parameters
emaLength = input(9, title="EMA Length")
ticks = input(100, title="Ticks")
profitPercent = input(75, title="Profit Percent (%)")
fastlen = input(12, title="MACD Fast Length")
slowlen = input(26, title="MACD Slow Length")
siglen = input(9, title="MACD Signal Length")

// Calculate Exponential Moving Average (EMA)
ema = ta.ema(close, emaLength)

// Calculate MACD
[macdLine, signalLine, _] = ta.macd(close, fastlen, slowlen, siglen)

// Determine if conditions for a long position are met
longCondition = ta.crossover(close, ema) and macdLine > signalLine

// Entry and Exit conditions
entryPrice = ta.highest(high, 2)[1]
stopLossPrice = ta.lowest(low, 2)[1]
targetPrice = entryPrice + ticks
profitPrice = entryPrice * (1 + profitPercent / 100)

// Plot signals on the chart
plotshape(longCondition, style=shape.triangleup, location=location.belowbar, color=color.green, size=size.small)
plotshape(longCondition and ta.crossover(macdLine, signalLine), style=shape.triangleup, location=location.belowbar, color=color.blue, size=size.small)

// Strategy logic
strategy.entry("Long", strategy.long, when=longCondition)
strategy.exit("StopLoss/Target", from_entry="Long", stop=stopLossPrice, limit=targetPrice)
strategy.exit("Profit", from_entry="Long", limit=profitPrice)
