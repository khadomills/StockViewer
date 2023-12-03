import os

import requests
import time
import sqlite3
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

load_dotenv()


class StockDataRetriever:
    # Static variable for the API key
    api_key = os.getenv("API_KEY")

    # Static variable for the stocks with their corresponding symbols
    stocks = {
        "Amazon": "AMZN",
        "Apple": "AAPL",
        "Dell": "DELL",
        "GameStop": "GME",
        "Google": "GOOGL",
        "HP": "HPQ",
        "Intel": "INTC",
        "Lyft": "LYFT",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "NVIDIA": "NVDA",
        "Tesla": "TSLA",
        "T-Mobile": "TMUS",
        "Uber": "UBER",
        "Verizon": "VZ",
    }

    # Method to fetch historical share data for all stocks
    def fetch_historical_data(self):
        # API endpoint URL
        url = "https://alpha-vantage.p.rapidapi.com/query"

        # Headers for the API request
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        # iteration variable for stock id
        stock_id = 0

        # Loop through each stock and fetch historical data
        for company, symbol in self.stocks.items():

            # Query parameters for the API request
            querystring = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "datatype": "json"}

            # Make the API request
            response = requests.get(url, headers=headers, params=querystring)

            # Connect to DB
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Process the data to json format
            data = response.json()

            # Check if 'message' header is present indicating error
            if 'message' in data:
                return -1, {data["message"]}

            # Iterate over each date in the API response
            for date, values in data['Time Series (Daily)'].items():
                # Convert the date to the required format
                date_formatted = date

                # Check if the date already exists in the database
                cursor.execute("SELECT COUNT(*) FROM stock_share_prices WHERE stock_id = ? AND time = ?",
                               (stock_id, date_formatted))
                count = cursor.fetchone()[0]

                # if count is 0, add share price data from that date into db
                if count == 0:

                    # Insert data into the 'stock_share_prices' table
                    cursor.execute('''
                                        INSERT INTO stock_share_prices (
                                            stock_id, time, open, high, low, close, volume
                                        ) VALUES ( ?, ?, ?, ?, ?, ?, ?);
                                    ''', (
                        stock_id,
                        date_formatted,
                        float(values['1. open']),
                        float(values['2. high']),
                        float(values['3. low']),
                        float(values['4. close']),
                        float(values['5. volume']),
                    ))

                # Data is up-to-date, return
                else:
                    print(f'Historical share price data now up to date for {company} ({symbol})')
                    break

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
            # Print a message indicating that data has been fetched
            print(f'Fetched Historical Share Data for {company} ({symbol})')

            # Add a delay to comply with API rate limits
            time.sleep(14)
            stock_id += 1

    # Method to fetch overview data for all stocks
    def fetch_overview_data(self):
        # API endpoint URL
        url = "https://alpha-vantage.p.rapidapi.com/query"

        # Headers for the API request
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        # iteration variable for stock id
        stock_id = 0

        # Loop through each stock and fetch overview data
        for company, symbol in self.stocks.items():
            # Query parameters for the API request
            querystring = {"function": "OVERVIEW", "symbol": symbol, "datatype": "json"}

            # Make the API request
            response = requests.get(url, headers=headers, params=querystring)

            # Process the data to json format
            data = response.json()

            # Check if 'message' header is present indicating error
            if 'message' in data:
                return -1, {data["message"]}

            # Connect to SQLite database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into the 'stocks' table
            query = '''
            INSERT OR REPLACE INTO stock_data (
                stock_id, symbol, name, desc, CIK, currency, country, sector, industry, address,
                fiscal_year_end, latest_qtr, market_capitalization, EBITDA, PERatio, PEGRatio,
                book_value, div_per_share, div_yield, EPS, rev_per_shareTTM, profit_margin,
                op_marginTTM, return_on_assetsTTM, return_on_equityTTM, revenueTTM, gross_profitTTM,
                dilutedEPSTTM, qtrly_earnings_growthYOY, qtrly_revenue_growthYOY, analyst_target_price,
                trailingPE, forwardPE, price_to_sales_ratioTTM, price_to_book_ratio, EV_to_revenue,
                EV_to_EBITDA, beta, week_high_52, week_low_52, day_moving_average_50,
                day_moving_average_200, shares_outstanding, div_date, ex_div_date, last_updated
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            '''

            # Get the current date for 'last_updated'
            current_date = datetime.now().strftime('%Y-%m-%d')

            # Execute the query
            cursor.execute(query, (
                stock_id,
                data['Symbol'],
                data['Name'],
                data['Description'],
                data['CIK'],
                data['Currency'],
                data['Country'],
                data['Sector'],
                data['Industry'],
                data['Address'],
                data['FiscalYearEnd'],
                data['LatestQuarter'],
                data['MarketCapitalization'],
                data['EBITDA'],
                data['PERatio'],
                data['PEGRatio'],
                data['BookValue'],
                data['DividendPerShare'],
                data['DividendYield'],
                data['EPS'],
                data['RevenuePerShareTTM'],
                data['ProfitMargin'],
                data['OperatingMarginTTM'],
                data['ReturnOnAssetsTTM'],
                data['ReturnOnEquityTTM'],
                data['RevenueTTM'],
                data['GrossProfitTTM'],
                data['DilutedEPSTTM'],
                data['QuarterlyEarningsGrowthYOY'],
                data['QuarterlyRevenueGrowthYOY'],
                data['AnalystTargetPrice'],
                data['TrailingPE'],
                data['ForwardPE'],
                data['PriceToSalesRatioTTM'],
                data['PriceToBookRatio'],
                data['EVToRevenue'],
                data['EVToEBITDA'],
                data['Beta'],
                data['52WeekHigh'],
                data['52WeekLow'],
                data['50DayMovingAverage'],
                data['200DayMovingAverage'],
                data['SharesOutstanding'],
                data['DividendDate'],
                data['ExDividendDate'],
                current_date,
            ))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            # Print a message indicating that data has been fetched
            print(f'Fetched Overview Data for {company} ({symbol})')

            # Add a delay to comply with API rate limits
            time.sleep(14)
            stock_id += 1

    # Method to fetch overview and historical share data for one stock.
    def fetch_one_stock(self, stock_id, symbol):

        # API endpoint URL
        url = "https://alpha-vantage.p.rapidapi.com/query"

        # Headers for the API request
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        # Query parameters for the API request
        querystring = {"function": "OVERVIEW", "symbol": symbol, "datatype": "json"}

        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)

        # Process the data to .json format
        data = response.json()
        # print(data)

        # Check if 'message' header is present indicating error
        if 'message' in data:
            return -1, {data["message"]}

        # Connect to SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Insert data into the 'stocks' table
        query = '''
        INSERT OR REPLACE INTO stock_data (
            stock_id, symbol, name, desc, CIK, currency, country, sector, industry, address,
            fiscal_year_end, latest_qtr, market_capitalization, EBITDA, PERatio, PEGRatio,
            book_value, div_per_share, div_yield, EPS, rev_per_shareTTM, profit_margin,
            op_marginTTM, return_on_assetsTTM, return_on_equityTTM, revenueTTM, gross_profitTTM,
            dilutedEPSTTM, qtrly_earnings_growthYOY, qtrly_revenue_growthYOY, analyst_target_price,
            trailingPE, forwardPE, price_to_sales_ratioTTM, price_to_book_ratio, EV_to_revenue,
            EV_to_EBITDA, beta, week_high_52, week_low_52, day_moving_average_50,
            day_moving_average_200, shares_outstanding, div_date, ex_div_date, last_updated
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

        # Get the current date for 'last_updated'
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Execute the query
        cursor.execute(query, (
            stock_id,
            data['Symbol'],
            data['Name'],
            data['Description'],
            data['CIK'],
            data['Currency'],
            data['Country'],
            data['Sector'],
            data['Industry'],
            data['Address'],
            data['FiscalYearEnd'],
            data['LatestQuarter'],
            data['MarketCapitalization'],
            data['EBITDA'],
            data['PERatio'],
            data['PEGRatio'],
            data['BookValue'],
            data['DividendPerShare'],
            data['DividendYield'],
            data['EPS'],
            data['RevenuePerShareTTM'],
            data['ProfitMargin'],
            data['OperatingMarginTTM'],
            data['ReturnOnAssetsTTM'],
            data['ReturnOnEquityTTM'],
            data['RevenueTTM'],
            data['GrossProfitTTM'],
            data['DilutedEPSTTM'],
            data['QuarterlyEarningsGrowthYOY'],
            data['QuarterlyRevenueGrowthYOY'],
            data['AnalystTargetPrice'],
            data['TrailingPE'],
            data['ForwardPE'],
            data['PriceToSalesRatioTTM'],
            data['PriceToBookRatio'],
            data['EVToRevenue'],
            data['EVToEBITDA'],
            data['Beta'],
            data['52WeekHigh'],
            data['52WeekLow'],
            data['50DayMovingAverage'],
            data['200DayMovingAverage'],
            data['SharesOutstanding'],
            data['DividendDate'],
            data['ExDividendDate'],
            current_date,
        ))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Print a message indicating that data has been fetched
        print(f'Fetched Overview Data for {stock_id} ({symbol})')

        # API endpoint URL
        url = "https://alpha-vantage.p.rapidapi.com/query"

        # Headers for the API request
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        # Query parameters for the API request
        querystring = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "datatype": "json"}

        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)

        # Connect to DB
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Process the data into json response
        data = response.json()

        # Check if 'message' header is present indicating error
        if 'message' in data:
            return -1, {data["message"]}

        # Iterate over each date in the API response
        for date, values in data['Time Series (Daily)'].items():
            # Convert the date to the required format
            date_formatted = date

            # Check if the date already exists in the database
            cursor.execute("SELECT COUNT(*) FROM stock_share_prices WHERE stock_id = ? AND time = ?",
                           (stock_id, date_formatted))
            count = cursor.fetchone()[0]

            # if count is 0, add share price data from that date into db
            if count == 0:

                # Insert data into the 'stock_share_prices' table
                cursor.execute('''                
                INSERT INTO stock_share_prices (
                    stock_id, time, open, high, low, close, volume
                ) VALUES (?, ?, ?, ?, ?, ?, ?);
                ''',
                               (
                                   stock_id,
                                   date_formatted,
                                   float(values['1. open']),
                                   float(values['2. high']),
                                   float(values['3. low']),
                                   float(values['4. close']),
                                   float(values['5. volume']),
                               ))

            # Data is up-to-date, return
            else:
                print(f'Historical share price data now up to date for {stock_id} ({symbol})')
                break

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Print a message indicating that data has been fetched
        print(f'Fetched Historical Share Data for {stock_id} ({symbol})')

        # Return success to flag
        return 1, "Success"
