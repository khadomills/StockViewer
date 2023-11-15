# Imports
import sqlite3
from flask import Flask, render_template, redirect, url_for
from StockDataRetriever import StockDataRetriever

# Create flask application object
app = Flask(__name__)


# Connect to database and return connection object
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Define the route for the about us page
@app.route('/about')
def about():
    return render_template('about.html')


# Define the route for the temporary stock index page
@app.route('/index') # Needs to be updated to homepage
def index():
    conn = get_db_connection()
    stock_data = conn.execute('SELECT * from stock_data').fetchall()
    return render_template('index.html', stock_data=stock_data)


# Define endpoint route for fetching all stock data, load into DB, and redirect to homepage
@app.route('/fetchalldata')
def fetchalldata():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_overview_data()
    api_grabber.fetch_historical_data()
    return redirect(url_for('about'))


# Define endpoint route for fetching company overview data, load into DB, and redirect to homepage
@app.route('/fetchoverviewdata')
def fetchoverviewdata():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_overview_data()
    return redirect(url_for('about'))


# Define endpoint route for fetching historical share data, load into DB, and redirect to homepage
@app.route('/fetchhistoricaldata')
def fetchhistoricaldata():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_historical_data()
    return redirect(url_for('about'))


@app.route('/graph.html')
def graph():
    return render_template('graph.html')


# Company detail view pages - Render detailed view template, fetch company overview stock data from db
@app.route('/AMZN')
def renderAMZNpage():
    return render_template('template.html', stock=grabstockdata(0))


@app.route('/AAPL')
def renderAAPLpage():
    return render_template('template.html', stock=grabstockdata(1))


@app.route('/DELL')
def renderDELLpage():
    return render_template('template.html', stock=grabstockdata(2))


@app.route('/GME')
def renderGMEpage():
    return render_template('template.html', stock=grabstockdata(3))


@app.route('/GOOGL')
def renderGOOGLpage():
    return render_template('template.html', stock=grabstockdata(4))


@app.route('/HPQ')
def renderHPQpage():
    return render_template('template.html', stock=grabstockdata(5))


@app.route('/INTC')
def renderINTCpage():
    return render_template('template.html', stock=grabstockdata(6))


@app.route('/LYFT')
def renderLYFTpage():
    return render_template('template.html', stock=grabstockdata(7))


@app.route('/MSFT')
def renderMSFTpage():
    return render_template('template.html', stock=grabstockdata(8))


@app.route('/NFLX')
def renderNFLXpage():
    return render_template('template.html', stock=grabstockdata(9))


@app.route('/NVDA')
def renderNVDApage():
    return render_template('template.html', stock=grabstockdata(10))


@app.route('/TSLA')
def renderTSLApage():
    return render_template('template.html', stock=grabstockdata(11))


@app.route('/TMUS')
def renderTMUSpage():
    return render_template('template.html', stock=grabstockdata(12))


@app.route('/UBER')
def renderUBERpage():
    return render_template('template.html', stock=grabstockdata(13))


@app.route('/VZ')
def renderVZpage():
    return render_template('template.html', stock=grabstockdata(14))


# Helper function to return company overview data from database
def grabstockdata(input_stock_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock_data INNER JOIN company_info ON stock_data.stock_id = company_info.stock_id WHERE stock_data.stock_id = ' + str(input_stock_id))
    stock = cursor.fetchone()
    return stock


# Run the flask application server
if __name__ == '__main__':
    app.run(debug=True)
