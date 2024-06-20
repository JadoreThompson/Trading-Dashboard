import MetaTrader5
import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta

load_dotenv('icmarkets.env')

mt5.initialize()

credentials ={
    'login': int(os.getenv('LOGIN')),
    'password': os.getenv('PASSWORD'),
    'server': os.getenv('SERVER')
}

print(mt5.login(credentials['login'], credentials['password'], credentials['server']))


today = date.today()

# have to make date to epoch and convert for output
trades = mt5.history_orders_get(14841879, 1718995479)
for trade in trades:
    if trade[6] == 1:
        print("Trade: ", trade[21])


