import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
from models import Chart_Trade


# Load environment variables
load_dotenv('icmarkets.env')

# Retrieve login credentials
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server = os.getenv('SERVER')

# logging in
authorised = mt5.initialize(login=int(login), password=password, server=server)

if authorised:
    print("Y")

# getting todays profit
def total_profit():
    ttl_profit = mt5.account_info()

    return ttl_profit


ttl_profit = total_profit()
ttl_profit = ttl_profit[10]
print("Total Profit: ", ttl_profit)


# getting 7 day growth
def weekly_profit():
    today = datetime.now()
    past_week = today - timedelta(weeks=1)
    deals = mt5.history_deals_get(past_week, today)
    formatted_deals = []

    for deal in deals:
        if deal[4] == 0:
            formatted_deal = {
                "ticket": deal.ticket,
                "order": deal.order,
                "time": deal.time,
                "time_msc": deal.time_msc,
                "type": deal.type,
                "entry": deal.entry,
                "magic": deal.magic,
                "position_id": deal.position_id,
                "reason": deal.reason,
                "volume": deal.volume,
                "price": deal.price,
                "commission": deal.commission,
                "swap": deal.swap,
                "profit": deal.profit,
                "fee": deal.fee,
                "symbol": deal.symbol,
                "comment": deal.comment,
                "external_id": deal.external_id
            }
            formatted_deals.append(formatted_deal)

    return formatted_deals


w_profit = weekly_profit()
prof = 0
for profit in w_profit:
    print("Profit: ", profit['profit'])
    prof = round(prof + profit['profit'], 2)

print("week's profit: ", prof)


# chart data
def chart_data():
    today = datetime.now()
    start_date = today - timedelta(weeks=2288)
    deals = mt5.history_deals_get(start_date, today)
    all_trades = []

    for deal in deals:
        if deal[4] == 0:
            formatted_deal = {
                "ticket": deal.ticket,
                "order": deal.order,
                "time": deal.time,
                "time_msc": deal.time_msc,
                "type": deal.type,
                "entry": deal.entry,
                "magic": deal.magic,
                "position_id": deal.position_id,
                "reason": deal.reason,
                "volume": deal.volume,
                "price": deal.price,
                "commission": deal.commission,
                "swap": deal.swap,
                "profit": deal.profit,
                "fee": deal.fee,
                "symbol": deal.symbol,
                "comment": deal.comment,
                "external_id": deal.external_id
            }
            all_trades.append(formatted_deal)

    account_balance = mt5.history_deals_get(start_date, today)
    for deal in account_balance:
        if deal[4] == 2:
            acc_balance = deal[13]

    return all_trades, acc_balance


all_trades, balance = chart_data()
chart_trades_list = []

i = 0
for trade in all_trades:
    time = trade['time']
    profit = trade['profit']

    trade = {
        'time': time,
        'profit': round((profit / balance) * 100, 2)
    }
    chart_trades_list.append(trade)

print("Balance", balance)
print("Everything", chart_trades_list)



mt5.shutdown()
