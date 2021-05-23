from stox.data import receive
from stox.predicter import run
import datetime as dt
import pandas as pd
import requests

def exec(stock, output='list', years=1, chart=False):

    techgood = False
    alreadygood = False
    techbad = False
    alreadybad = False

    stock_data = receive(stock, years=years)
    data = stock_data
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(stock)
    company = requests.get(url).json()['ResultSet']['Result'][0]['name']

    techgood = False
    alreadygood = False
    techbad = False
    alreadybad = False

    df = data.iloc[-3:]

    df.to_csv('df.csv')
    df = pd.read_csv('df.csv')

    cu = df.at[2,'RSIUP']
    cy = df.at[1,'RSIUP']
    su = df.at[2,'PRICEUP']
    sy = df.at[1,'PRICEUP']

    bu = df.at[2,'RSIDOWN']
    by = df.at[1,'RSIDOWN']
    du = df.at[2,'PRICEDOWN']
    dy = df.at[1,'PRICEDOWN']

    cmp = df.at[2,'Close']

    if cu == True & su == True:
        if cy == False or sy == False:
            techgood = True
        else:
            alreadygood = True
    elif bu == True & du == True:
        if by == False or dy == False:
            techbad = True
        else:
            alreadybad = True

    cmp = df.at[2,'Close']

    result, y_predicted, df = run(stock_data, [], 1, 0.9)

    date = (dt.datetime.today() + dt.timedelta(days=1))
    while date.weekday() == 5 or date.weekday() == 6:
        date = date + dt.timedelta(days=1)
    date = date.strftime('%Y-%m-%d')
    if techgood == True:
        result.append("Bullish (Starting)")
    elif alreadygood == True:
        result.append("Bullish (Already)")
    elif techbad == True:
        result.append("Bearish (Starting)")
    elif alreadybad == True:
        result.append("Bearish (Already)")
    else:
        result.append("None")
    result.append(cmp)
    result.append(date)

    priceprediction = result[0]
    techanalysis = result[1]
    ltp = result[2]
    datefor = result[3]
    result = []
    result = result+[company]
    result = result+[ltp]
    result = result+[priceprediction]
    result = result+[techanalysis]
    result = result+[datefor]

    if output == 'list':
        result = result
    elif output == 'message':
        result = f'''
Company Name = {company}
Current Price = {ltp}
Predicted Price = {priceprediction}
Technical Analysis = {techanalysis}
Data (For) = {datefor}'''

    if not chart:
        return result

    if chart:
        dates = df.index.tolist()
        from pandas.plotting import register_matplotlib_converters
        register_matplotlib_converters()
        import matplotlib.pyplot as plt
        plt.plot(dates, y_predicted)
        plt.plot(dates, df.Close.tolist())
        plt.title(stock + ' - %1.2f' % result[0] + ' - %1.3f' % result[1] + '% - ' + result[2])
        plt.xlabel('Date')
        plt.ylabel('Close price (USD)')
        plt.legend(['Predicted', 'True'])
        plt.gcf().autofmt_xdate()
        plt.show()

        return result
