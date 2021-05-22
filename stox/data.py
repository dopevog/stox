import pandas as pd
from pandas_datareader import data
import datetime as dt
import pandas_ta 
from pytrends.request import TrendReq


def main(stock, years=1):  
    end = dt.datetime.today().strftime('%Y-%m-%d') 
    start = (dt.datetime.today() - dt.timedelta(days=365*years)).strftime('%Y-%m-%d') 
    df = data.DataReader(stock, 'yahoo', start, end)

    return df, start, end

def add_rsi(df):
    close = df["Close"]    
    df['RSI'] = pandas_ta.momentum.rsi(close, length=None, scalar=None, drift=None, offset=None)

    return df

def add_ma50(df):
    df['MA50'] = df.Close.rolling(50, min_periods=1).mean()

    return df

def receive(stock, years=1, indicators=True):
    df, start, end = main(stock, years=years) 

    if indicators: 
        df = add_rsi(df)  
        df = add_ma50(df)
        df['RSIUP'] = df.RSI>50
        df['PRICEUP'] = df.Close>df.MA50
        df['RSIDOWN'] = df.RSI<50
        df['PRICEDOWN'] = df.Close<df.MA50

    df = df.dropna()   

    return df


def correlation(stock, years=1, indicators=True, period=14, complete=True, limit=0.5):

    df = receive(stock, years, indicators, period)

    if complete:
        features = df.corr().Close
    else:  
        features = df.corr().Close[df.corr().Close > limit].index.tolist()

    return features
