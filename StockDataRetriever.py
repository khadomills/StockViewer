import requests
import time
import sqlite3
from datetime import datetime


class StockDataRetriever:

    # Static variable for the API key
    api_key = "6dc4b895bdmshcff1c01a07c300ep1ee1b4jsn3733ec473c54"

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

            # Process the data as needed (e.g., print or store in a database)
            data = response.json()
            print(data)




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

            if symbol == 'GME':
                stock_id += 1
                continue

            # Process the data as needed (e.g., print or store in a database)
            data = response.json()
            print(data)

            # Connect to SQLite database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert data into the 'stocks' table
            query = '''
            INSERT INTO stock_data (
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
                int(data['MarketCapitalization']),
                int(data['EBITDA']),
                float(data['PERatio']),
                float(data['PEGRatio']),
                float(data['BookValue']),
                float(data['DividendPerShare']),
                float(data['DividendYield']),
                float(data['EPS']),
                float(data['RevenuePerShareTTM']),
                float(data['ProfitMargin']),
                float(data['OperatingMarginTTM']),
                float(data['ReturnOnAssetsTTM']),
                float(data['ReturnOnEquityTTM']),
                int(data['RevenueTTM']),
                int(data['GrossProfitTTM']),
                float(data['DilutedEPSTTM']),
                float(data['QuarterlyEarningsGrowthYOY']),
                float(data['QuarterlyRevenueGrowthYOY']),
                float(data['AnalystTargetPrice']),
                float(data['TrailingPE']),
                float(data['ForwardPE']),
                float(data['PriceToSalesRatioTTM']),
                float(data['PriceToBookRatio']),
                float(data['EVToRevenue']),
                float(data['EVToEBITDA']),
                float(data['Beta']),
                float(data['52WeekHigh']),
                float(data['52WeekLow']),
                float(data['50DayMovingAverage']),
                float(data['200DayMovingAverage']),
                int(data['SharesOutstanding']),
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
