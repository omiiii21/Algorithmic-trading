//@version=4
strategy("VWAP Strategy", shorttitle="VWAP Strategy", overlay=true)

// VWAP Calculation
vwapLength = input(20, title="VWAP Length")
vwap = sma(close * volume, vwapLength) / sma(volume, vwapLength)

// Entry Conditions
longCondition = crossover(close, vwap)
shortCondition = crossunder(close, vwap)

// Plot VWAP
plot(vwap, color=color.blue, title="VWAP")

// Plot Entry Signals
plotshape(series=longCondition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Define Stop Loss and Take Profit
stopLossPercent = input(1, title="Stop Loss (%)", minval=0.1, maxval=5, step=0.1)
takeProfitPercent = input(1, title="Take Profit (%)", minval=0.1, maxval=5, step=0.1)

stopLossPrice = close * (1 - stopLossPercent / 100)
takeProfitPrice = close * (1 + takeProfitPercent / 100)

strategy.entry("Long", strategy.long, when = longCondition)
strategy.entry("Short", strategy.short, when = shortCondition)

strategy.exit("Take Profit/Stop Loss", from_entry="Long", stop=stopLossPrice, limit=takeProfitPrice)
strategy.exit("Take Profit/Stop Loss", from_entry="Short", stop=stopLossPrice, limit=takeProfitPrice)
