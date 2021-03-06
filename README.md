<h1 align="center" style="border-bottom: none">
    <b>
        <a href="https://pypi.org/project/stox/">Stox </a><br>
    </b>
    <img align="center" width="100" height="100" src="https://github.com/cstox/stox/blob/main/favicon.png"><br>
    </b>
    ⚡ A Python Module For The Stock Market ⚡ <br>

</h1>

A Module to predict the "close price" for the next day and give "technical analysis". It 
 uses a Neural Network and the LSTM algorithm to predict the price. It uses a technical 
 indicator algorithm developed by the Stox team for technical analysis. 

## Installation
Get it from [PyPi](https://pypi.org/project/stox/):
```
pip3 install stox
```
Clone it from github:
```
git clone https://github.com/dopevog/stox.git
cd stox
python3 setup.py install
```

## Usage
### Arguments:
```
    stock (str): stock ticker symbol
    output (str): 'list' or 'message' (Format Of Output)
    years (int or float): years of data to be considered
    chart (bool): generate performance plot
```

### Returns:
List: 
```
[company name, current price, predicted price, technical analysis, date (For)]
```
Message:
```
company name
current price
predicted price
technical analysis
data (for)
```

### Examples:
#### Basic
```
import stox

script = input("Stock Ticker Symbol: ")
data = stox.stox.exec(script,'list')

print(data)
```
```
$ stox> python3 main.py
$ Stock Ticker Symbol: AAPL
$ ['Apple Inc.', 125.43000030517578, 124.91, 'Bearish (Already)', '2021-05-24']
```
#### Intermediate
```
import stox
import pandas as pd

stock_list = pd.read_csv("SPX500.csv") 
df = stock_list 
number_of_stocks = 505 
x = 0
while x < number_of_stocks:
    ticker = stock_list.iloc[x]["Symbols"]
    data = stox.stox.exec(ticker,'list')
    df['Price'] = data[1] 
    df['Prediction'] = data[2]
    df['Analysis'] = data[3]
    df['DateFor'] = data[4]
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
df.to_csv("output.csv") 
print("Done") 
```
```
$ stox> python3 main.py
$ Done
```
#### More Examples Including These Ones Can Be Found [Here](https://github.com/cstox/stox/tree/main/Examples)

### Possible Implentations
* Algorithmic Trading
* Single Stock Analysis
* Multistock Analysis
* And Much More!

## Credits
* [Dopevog](https://github.com/dopevog)
* [Gerard López](https://macosicons.com/u/Gerard%20L%C3%B3pez) - Logo

## License
This Project Has Been [MIT Licensed](https://github.com/cstox/stox/blob/main/License.txt)
