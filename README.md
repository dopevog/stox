# Stox
 A Module to predict the "close price" for the next day and give "technical analysis". It 
 uses a Neural Network and the LSTM algorithm to predict the price. It uses a technical 
 indicator algorithm developed by the Stox team for technical analysis. Check out how it works [here](https://github.com/cstox/stox/blob/main/Workings.md).

## Installation
Get it from [PyPi](https://pypi.org/project/stox/):
```
pip3 install stox
```
Clone it from github:
```
git clone https://github.com/dopevog/stox.git
cd stox
python3 setup.py
```

## Usage
### Arguments:
```
    stock (str): stock label
    output (str): 'list' or 'message'
    steps (int): previous days to consider for generating the model.
    training (float): fraction assigned for training the model
    years (int or float): years of data to be considered
    plot (bool): generate performance plot
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
data = stox.stox.exec(script,'message')

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

## License
This Project Has Been [MIT Licensed](https://github.com/cstox/stox/blob/main/License.txt)
