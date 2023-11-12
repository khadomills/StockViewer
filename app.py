import sqlite3

from flask import Flask, render_template, redirect, url_for
from StockDataRetriever import StockDataRetriever

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Define the route for the homepage
@app.route('/')
def homepage():
    return 'Welcome to the homepage!'


# Define the route for the about page
@app.route('/about')
def about():
    return 'This is the about page.'


# Define the route for the stock info page
@app.route('/stock')
def stock_info():
    return 'Stock information page.'


# define the route for the temporary stock index page
@app.route('/index')
def index():
    conn = get_db_connection()
    stock_data = conn.execute('SELECT * from stock_data').fetchall()
    return render_template('index.html', stock_data=stock_data)


@app.route('/testoverviewgrabber')
def testoverviewgrabber():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_overview_data()

    return redirect(url_for('index'))


@app.route('/testhistoricalgrabber')
def testhistoricalgrabber():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_historical_data()

@app.route('/redirecttest')
def redirecttest():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
