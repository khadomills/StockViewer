# Stock Viewer Project

---------------------
## Overview
---------------------
The Stock Viewer is a web application designed for personal investors and financial enthusiasts to track and view details of various prominent stocks. 
This application provides daily up-to-date information on 15 major companies, leveraging the Flask framework for the backend, Bootstrap for a responsive front-end design, and SQLite3 for efficient data storage.
<br><br>The 15 Stocks shown in this application are:<br>
Amazon: AMZN<br>
Apple: AAPL<br>
Dell: DELL<br>
GameStop: GME<br>
Google Class A: GOOGL<br>
HP: HPQ<br>
Intel: INTC<br>
Lyft: LYFT<br>
Microsoft: "MSFT<br>
Netflix: "NFLX<br>
NVIDIA: "NVDA<br>
Tesla: TSLA<br>
T-Mobile: TMUS<br>
Uber: UBER<br>
Verizon: VZ<br>

---------------------
## Features
---------------------
Stock Information: View real-time data on stocks like Dell, GameStop, Alphabet, and more.<br>
Responsive Design: Utilizing Bootstrap, the app offers a seamless experience on both desktop and mobile devices.<br>
Data Persistence: Uses SQLite3 to store and retrieve stock data efficiently.

---------------------
## Prerequisites / Deployment
---------------------

Before you begin, ensure you have met the following requirements:<br>
Python 3.x<br>
Flask<br>
SQLite3<br>
An API key from [Rapid API: https://rapidapi.com/alphavantage/api/alpha-vantage/pricing]<br>

### Installation:
To install the Stock Viewer, follow these steps:<br>
Clone the repo:

    git clone https://github.com/khadomills/StockViewer.git
Install the necessary Python packages:

    pip install -r requirements.txt
### Setup:
Set your API key in the environment variables:<br>
create a .env file in the project folder add the code below with your API from Rapid API

    API_KEY = "ADD YOUR API KEY HERE"
Initialize the SQLite3 database:

    python init_db.py
### Running the Application:
To run the Stock Viewer, use the following command:

    flask run
The application will be available at http://localhost:5000.

## Contributing
We welcome contributions to the Stock Viewer Project. <br>If you have suggestions or improvements, please fork the repository and create a pull request.

