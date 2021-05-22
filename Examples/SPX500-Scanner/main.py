import stox
import pandas as pd

stock_list = pd.read_csv("SPX500.csv")
df = stock_list
number_of_stocks = 100
x = 0
while x < number_of_stocks:
    ticker = stock_list.iloc[x]["Symbols"]
    data = stox.stox.exec(script,'list')
    df['Price'] = data[1]
    df['Prediction] = data[2]
    df['Analysis] = data[3]
    df['DateFor'] = data[4]
    if df.Prediction - df.Price >= df.Price * 0.02:
        if df.Analysis == "Bullish (Starting)":
            df['Signal'] = "Buy"
        elif df.Analysis == "Bullish (Already)":
            df['Signal'] = "Up"
    elif df.Prediction - df.Price <= df.Price * -0.02:
        if df.Analysis == "Bearish (Starting)":
            df['Signal'] = "Sell"
        elif df.Analysis == "Bearish (Already)":
            df['Signal'] = "Down"
    else:
        df['Signal'] = "None"
    x = x+1
df.to_csv("output.csv")
print("Done")
