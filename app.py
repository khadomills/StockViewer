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


# Define the default route for the index page
@app.route('/')
def default():
    return redirect(url_for('index'))


# Define the route for the about us page
@app.route('/about')
def about():
    return render_template('about.html', share_price_data=grabpricedata())


# Define the route for the temporary stock index page
@app.route('/index')  # Needs to be updated to homepage
def index():
    # Render page
    return render_template('index.html', share_price_data=grabpricedata())


# Define endpoint route for fetching all stock data, load into DB, and redirect to homepage
@app.route('/fetchalldata')
def fetchalldata():
    api_grabber = StockDataRetriever()
    api_grabber.fetch_overview_data()
    api_grabber.fetch_historical_data()
    return redirect(url_for('index'))


# Define endpoint route for fetching company overview data, load into DB, and redirect to homepage
@app.route('/fetchoverviewdata')
def fetchoverviewdata():
    # Create API grabber object and refresh all overview data for every stock
    api_grabber = StockDataRetriever()
    flag = api_grabber.fetch_overview_data()

    # Check if flag contains negative response, redirect to error page output message
    if flag[0] == -1:
        print(flag[1])
        return redirect(url_for('error', error_message=flag[1], symbol='index'))

    # Render homepage
    return redirect(url_for('index'))


# Define endpoint route for fetching historical share data, load into DB, and redirect to homepage
@app.route('/fetchhistoricaldata')
def fetchhistoricaldata():
    # Create API grabber object and refresh all historical share data for every stock
    api_grabber = StockDataRetriever()
    flag = api_grabber.fetch_historical_data()

    # Check if flag contains negative response, redirect to error page output message
    if flag[0] == -1:
        print(flag[1])
        return redirect(url_for('error', error_message=flag[1], symbol='index'))

    # Render homepage
    return redirect(url_for('index'))


# Route for API error page
@app.route('/error/<error_message>/<symbol>')
def error(error_message, symbol):
    return render_template('error.html', error_message=error_message, symbol=symbol)


# Company detail view pages - Render detailed view template, fetch company overview stock data from db
@app.route('/AMZN')
def renderAMZNpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(0)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/AAPL')
def renderAAPLpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(1)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/DELL')
def renderDELLpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(2)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/GME')
def renderGMEpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(3)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/GOOGL')
def renderGOOGLpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(4)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/HPQ')
def renderHPQpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(5)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/INTC')
def renderINTCpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(6)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/LYFT')
def renderLYFTpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(7)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/MSFT')
def renderMSFTpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(8)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/NFLX')
def renderNFLXpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(9)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/NVDA')
def renderNVDApage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(10)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/TSLA')
def renderTSLApage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(11)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/TMUS')
def renderTMUSpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(12)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/UBER')
def renderUBERpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(13)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


@app.route('/VZ')
def renderVZpage():
    # Pull all stock data from DB and render detailed page template.
    data = grabstockdata(14)
    return render_template('template.html', stock=data[0], share_data=data[1], share_price_data=grabpricedata())


# Route for stock update button
@app.route('/update_stock/<int:stock_id>/<string:symbol>')
def update_stock(stock_id, symbol):
    # Create API grabber object and refresh stock
    api_grabber = StockDataRetriever()
    flag = api_grabber.fetch_one_stock(stock_id, symbol)

    # Check if flag contains negative response, redirect to error page output message
    if flag[0] == -1:
        error_message = flag[1]
        print(error_message)

        # Redirect to error message page
        return redirect(url_for('error', error_message=error_message, symbol=symbol))
    else:
        print(flag[1])

    return redirect(url_for('render' + symbol + 'page'))


# Helper function to return company overview / info data from database
def grabstockdata(input_stock_id):
    # Get connection and create cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # execute query and return tuple for company and financial information
    cursor.execute(
        'SELECT * FROM stock_data INNER JOIN company_info ON stock_data.stock_id = company_info.stock_id WHERE stock_data.stock_id = ' + str(
            input_stock_id))
    stock = cursor.fetchone()

    # execute query and return historical share data
    cursor.execute(
        'SELECT time, open, high, low, close FROM stock_share_prices WHERE stock_id = ' + str(
            input_stock_id) + ' ORDER BY time'
    )
    share_data = cursor.fetchall()

    # Create a list to store the formatted data
    formatted_share_data = []

    # Iterate over the rows and format the data
    for row in share_data:
        time, open_price, high_price, low_price, close_price = row
        formatted_row = {
            'time': str(time),  # Convert time to string if it's not already
            'open': float(open_price),
            'high': float(high_price),
            'low': float(low_price),
            'close': float(close_price)
        }
        formatted_share_data.append(formatted_row)

    # Return stock data
    return stock, formatted_share_data


def grabpricedata():
    # Get connection and create cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the last loaded share price date
    cursor.execute('SELECT MAX(time) from stock_share_prices')
    last_update = cursor.fetchone()[0]

    # Fetch share price data for given date
    cursor.execute('SELECT * from stock_share_prices WHERE time = \'' + last_update + '\'')
    share_price_data = cursor.fetchall()

    # Return tuple
    return share_price_data


# Run the flask application server
if __name__ == '__main__':
    app.run(debug=True)
