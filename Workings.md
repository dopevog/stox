# How This Module Works
## The Price Prediction
For predicting the next closing price, Stox uses the [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) algorithm, which is a type of [ANN](https://en.wikipedia.org/wiki/Artificial_neural_network). Below is a pictorial representation of how it functions:

![image](https://user-images.githubusercontent.com/82938580/119778432-260b6000-bee5-11eb-9451-356e00b29990.png)
## The Technical Analysis
For technical analysis, Stox uses the [RSI]() and [Moving Average]() indicators. The algorithm it uses was developed by [Dopevog]() and is very accurate (97%). The algorithm is below:

```
RSI crosses 50 & MA50 below price 
or
RSI above 50 & MA50 breaches price
= Uptrend (Start)
```
```
RSI above 50 & MA50 below price 
= Uptrend (Already)
```
```
RSI breaches 50 & MA50 above price 
or
RSI below 50 & MA50 crosses price
= Downtrend (Start)
```
```
RSI below 50 & MA50 above price 
= Uptrend (Start)
```
