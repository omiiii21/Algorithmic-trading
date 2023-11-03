//@version=4
strategy("RSI Strat", overlay=true)

// RSI parameters
rsiLength = input(14, "RSI Length")
rsiOverbought = input(70, "RSI Overbought Level")
rsiOversold = input(30, "RSI Oversold Level")

// Calculate RSI
rsiValue = ta.rsi(close, rsiLength)

// Generate buy and sell signals
isOverbought = rsiValue > rsiOverbought
isOversold = rsiValue < rsiOversold

// Entry conditions
strategy.entry("Buy", strategy.long, when=isOversold)
strategy.entry("Sell", strategy.short, when=isOverbought)

// Exit conditions
strategy.close("Buy", when=isOverbought)
strategy.close("Sell", when=isOversold)
