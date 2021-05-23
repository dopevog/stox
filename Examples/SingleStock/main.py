## Import The Modules
import stox

script = input("Stock Ticker Symbol: ") ## Take Input Of Ticker Symbol
data = stox.stox.exec(script,'message') ## Get Result From Stox

print(data) ## Give Output As Message