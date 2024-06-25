from flask import Blueprint, render_template, redirect, url_for
import MetaTrader5
import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta


views = Blueprint('views', __name__)

mt5.initialize()
credentials = {
    'login': int(os.getenv('LOGIN')),
    'password': os.getenv('PASSWORD'),
    'server': os.getenv('SERVER')
}

from_date = datetime(1970,6,1)
today = date.today()


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')