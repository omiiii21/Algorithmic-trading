//@version=5
strategy("MACD Strategy", shorttitle="MACD", overlay=true)

// MACD parameters
fastLength = input(12, title="Fast EMA Length")
slowLength = input(26, title="Slow EMA Length")
signalSMA = input(9, title="Signal EMA Length")

[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalSMA)

// Entry conditions
longCondition = ta.crossover(macdLine, signalLine)
shortCondition = ta.crossunder(macdLine, signalLine)

// Plot MACD lines on the chart
plot(macdLine, title="MACD Line", color=color.blue)
plot(signalLine, title="Signal Line", color=color.red)

// Plot entry signals
plotshape(series=longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Set strategy orders
strategy.entry("Long", strategy.long, when = longCondition)
strategy.entry("Short", strategy.short, when = shortCondition)
