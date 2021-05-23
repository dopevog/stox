## Import The Modules
import stox
import pandas as pd

stock_list = pd.read_csv("SPX500.csv") ## Read Stock Ticker List CSV
df = stock_list ## Store It As A Variable
number_of_stocks = 505 ## Number Of Tickers In CSV
x = 0
while x < number_of_stocks:
    ticker = stock_list.iloc[x]["Symbols"] ## Get The Current Ticker Symbol
    data = stox.stox.exec(ticker,'list') ## Get Analysis From Stox
    ## Import All Needed Data (Price, Prediction, Analysis, etc.)
    df['Price'] = data[1] 
    df['Prediction'] = data[2]
    df['Analysis'] = data[3]
    df['DateFor'] = data[4]
    ## Run Scan For Buy/Up/Down/Sell
    if data[2] - data[1]  >= data[1]  * 0.02:
        if data[3] == "Bullish (Starting)":
            df['Signal'] = "Buy"
        elif data[3] == "Bullish (Already)":
            df['Signal'] = "Up"
    elif data[2] - data[1]  <= data[1]  * -0.02:
        if data[3] == "Bearish (Starting)":
            df['Signal'] = "Sell"
        elif data[3] == "Bearish (Already)":
            df['Signal'] = "Down"
    else:
        df['Signal'] = "None"
    x = x+1
df.to_csv("output.csv") ## Export To CSV
print("Done") ## Print 'Done' After Complete
