## Import The Modules
import stox
import pandas as pd

stock_list = ['FB','AAPL','AMZN','NFLX','GOOG'] ## List Of Stocks You Would Want To Buy 
number_of_stocks = len(stock_list)
print(number_of_stocks)
x = 0
starting_cash = 10000 ## Amount Of Money In Trading Account
current_cash = starting_cash
percent_to_spend = 5
money_to_spend = (5/100)*percent_to_spend

def buy(ticker, price, amt):
    ## Here Add Use Your Brocker's API To Buy
    cost = price*amt
    brockerage = 0.1 ## Your Brockerage %
    brockerage = brockerage/100 ## Convert To Decimel
    cost = cost + (cost*brockerage) ## Get Total Cost
    current_cash = current_cash - cost
    print("Bought!")
    return current_cash

def short(ticker, price, amt):
    ## Use Your Brocker's API To Short
    cost = price*amt
    brockerage = 0.1 ## Your Brockerage %
    brockerage = brockerage/100 ## Convert To Decimel
    cost = cost + (cost*brockerage) ## Get Total Cost
    current_cash = current_cash - cost
    print("Shorted!")
    return current_cash

while x < number_of_stocks:
    ticker = stock_list[x] ## Get The Current Ticker Symbol
    data = stox.stox.exec(ticker,'list') ## Get Analysis From Stox
    ## Import All Needed Data (Price, Prediction, Analysis, etc.)
    df = pd.DataFrame()
    df['Ticker'] = ticker
    df['Price'] = data[1] 
    df['Prediction'] = data[2]
    df['Analysis'] = data[3]
    df['DateFor'] = data[4]
    good_pct = data[1]*0.02 
    minus_pct = good_pct*-1
    ## Run Scan For Buy/Up/Down/Sell
    if data[2] - data[1] >= good_pct:
        if data[3] == "Bullish (Starting)":
            df['Signal'] = "Buy"
            if money_to_spend <= current_cash: ## Check If Enough Money Left
                price = df.Price
                amt = price
                current_cash = buy(ticker, price, amt) ## Call Buy Function
                print("Bought "+ticker)
            else:
                print("Not Enough Money Left!")
        elif data[3] == "Bullish (Already)":
            df['Signal'] = "Up"
            print(ticker+" is in a Uptrend")
    elif data[2] - data[1] <= minus_pct:
        if data[3] == "Bearish (Starting)": 
            df['Signal'] = "Sell"
            if money_to_spend <= current_cash: ## Check If Enough Money Left
                price = df.Price
                amt = price
                current_cash = short(ticker, price, amt) ## Call Short Function
                print("Shorted "+ticker)
            else:
                print("Not Enough Money Left!")
        elif data[3] == "Bearish (Already)":
            df['Signal'] = "Down"
            print(ticker+" is in a Downtrend")
    else:
        df['Signal'] = "None"
        print("No Signal For "+ticker)
    x = x+1
print("Done") ## Print 'Done' After Complete
