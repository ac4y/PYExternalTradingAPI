from ib_insync import *
import datetime

from src.external_trading_api.client.ib_api import InteractiveBrokersAPI

interactiveBrokersAPI = InteractiveBrokersAPI()

print(interactiveBrokersAPI.get_set_api())

contract = Forex('EURUSD')
bars = interactiveBrokersAPI.get_api().reqHistoricalData(
    contract, endDateTime='', durationStr='1 D',
    barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe:
df = util.df(bars)
print(df)
print(datetime.datetime.now())

