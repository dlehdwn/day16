def sol(numbers):
    numList = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for index, items in enumerate(numList):
        numbers = numbers.replace(items,str(index))
    return int(numbers)

print(sol("onefoursixonezerosevennine")) #1461079

import ccxt

exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']

newCurrent_price = current_price

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"BTC/USD 현재 가격 : {current_price}")
    if newCurrent_price - current_price > 0:
        print("제발 도망쳐")
    else:
        print("떡상 가자")



