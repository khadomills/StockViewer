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

    return redirect(url_for('index'))

@app.route('/redirecttest')
def redirecttest():
    return redirect(url_for('index'))

@app.route('/graph.html')
def graph():
        return render_template('graph.html')

# Company detail pages
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

# Template for rendering detailed stock pages given parameter stock_id
def grabstockdata(uStock_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock_data INNER JOIN company_info ON stock_data.stock_id = company_info.stock_id WHERE stock_data.stock_id = ' + str(uStock_id))
    stock = cursor.fetchone()
    return stock


if __name__ == '__main__':
    app.run(debug=True)
