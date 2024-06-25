from flask import Flask
from views import views
import os
from dotenv import load_dotenv
import MetaTrader5 as mt5

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

app = Flask(__name__)
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
