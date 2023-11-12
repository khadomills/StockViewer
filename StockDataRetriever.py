import requests
import time
import sqlite3


class StockDataRetriever:

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row

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

            # Process the data as needed (e.g., print or store in a database)

            # Print a message indicating that data has been fetched
            print(f'Fetched Overview Data for {company} ({symbol})')

            # Add a delay to comply with API rate limits
            time.sleep(14)
            stock_id +=1
