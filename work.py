import asyncio
import pandas as pd
from binance.client import Client
import datetime as dt# client configuration
from time import sleep
from binance import AsyncClient
from binance import AsyncClient, BinanceSocketManager

#Demo Binance Account >>
api_key = 'YstNFttSJG5nAftDPVTFJAqR6Ro4SMjyXFaXXMNcGmOwd9C6WI7EG0HAwfgCvLip'
api_secret = 'O4tVRt6SyFSbEWJcu98jOd9VxnuZSAJEDotRbJv6UFaNXEwaxGFruA9fbF7I1LJC'
client = Client(api_key, api_secret)

async def kline_listener(client):
    bm = BinanceSocketManager(client)
    symbol = 'XRPUSDT'
    res_count = 0
    async with bm.kline_socket(symbol=symbol) as stream:
        while True:
            res = await stream.recv()
            res_count += 1
            #print(res)
            #if res_count == 2:
            res_count = 0
            order_book = await client.get_symbol_ticker(symbol=symbol)

            print(order_book)
            Fallen()



async def main():

    client = await AsyncClient.create()
    await kline_listener(client)
def Fallen():
    df = getHour()
    cumulret = (df.Open.pct_change() + 1).cumprod() - 1
    if cumulret[-1] > -0.01:
        print("price Has Fallen By 1%")


#Really Now!!

def getHour():
    frame = pd.DataFrame(client.get_historical_klines('XRPUSDT', '1m', '30 min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index,unit='ms')
    frame = frame.astype(float)
    return frame



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


