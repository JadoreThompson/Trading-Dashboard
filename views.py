from flask import Blueprint, render_template, redirect, url_for
import MetaTrader5
import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta


views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/dashboard')
def dashboard():
    def total_profit():
        ttl_profit = mt5.account_info()

        return ttl_profit

    ttl_profit = total_profit()
    if ttl_profit is None:
        ttl_profit = 0
    else:
        ttl_profit = ttl_profit[10]
        print(ttl_profit)

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

    currency = mt5.account_info()
    currency = currency[26]


    return render_template('dashboard.html', ttl_profit=ttl_profit, w_profit=prof,
                           currency=currency)