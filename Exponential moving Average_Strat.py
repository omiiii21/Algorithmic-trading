//@version=5
strategy("EMA Strategy with Buy/Sell Signals", overlay=true)

// EMA parameters
emaLength = input(14, title="EMA Length")
fastEma = ta.ema(close, emaLength)
slowEma = ta.ema(close, 2 * emaLength)

// Entry conditions
longCondition = ta.crossover(fastEma, slowEma)
shortCondition = ta.crossunder(fastEma, slowEma)

// Plot EMA lines on the chart
plot(fastEma, title="Fast EMA", color=color.blue)
plot(slowEma, title="Slow EMA", color=color.red)

// Plot buy and sell signals
plotshape(series=longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Buy and Sell signals for strategy
strategy.entry("Buy", strategy.long, when = longCondition)
strategy.entry("Sell", strategy.short, when = shortCondition)
