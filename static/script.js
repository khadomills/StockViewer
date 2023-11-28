const companies = {
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
};

function createStockWidget(symbol, name) {
    const widget = document.createElement('div');
    widget.className = 'stock-widget';
    widget.innerHTML = `
        <div class="stock-summary" onclick="toggleCard('${symbol}')">
            <img src="logos/${symbol.toLowerCase()}.jpg" alt="${name} Logo" class="stock-logo">
            <div class="stock-info">
                <span>${name} (${symbol})</span>
                <span id="company-price-${symbol}">-- USD</span>
                <span id="price-change-${symbol}" class="price-change">(--%)</span>
            </div>
        </div>
        <div id="stock-card-${symbol}" class="stock-card">
            <!-- Detailed stats will be populated here -->
        </div>
    `;
    return widget;
}

function toggleCard(symbol) {
    const stockCard = document.getElementById(`stock-card-${symbol}`);
    stockCard.classList.toggle('toggled');
}

function fetchStockData(symbol) {
    const apiKey = 'QEHLSEQZWQ0SZGJA';
    const overviewUrl = `https://www.alphavantage.co/query?function=OVERVIEW&symbol=${symbol}&apikey=${apiKey}`;
    const quoteUrl = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${apiKey}`;

    Promise.all([
        fetch(overviewUrl).then(response => response.json()),
        fetch(quoteUrl).then(response => response.json())
    ]).then(([overviewData, quoteData]) => {
        const quote = quoteData['Global Quote'];
        updateStockSummary(symbol, quote);
        updateStockCard(symbol, overviewData, quote);
    }).catch(error => console.error('Error fetching data:', error));
}


function formatLargeNumber(value) {
    if (value >= 1e12) {
        return (value / 1e12).toFixed(2) + 'T';
    } else if (value >= 1e9) {
        return (value / 1e9).toFixed(2) + 'B';
    } else if (value >= 1e6) {
        return (value / 1e6).toFixed(2) + 'M';
    } else {
        return value.toLocaleString();
    }
}

function updateStockSummary(symbol, quote) {
    const price = parseFloat(quote['05. price']).toFixed(2);
    const change = parseFloat(quote['09. change']).toFixed(2);
    const changePercent = parseFloat(quote['10. change percent']).toFixed(2);

    const priceElement = document.getElementById(`company-price-${symbol}`);
    const changeElement = document.getElementById(`price-change-${symbol}`);

    priceElement.textContent = `${price} USD`;
    changeElement.textContent = `${change} (${changePercent}%)`;

    // Apply different classes based on positive or negative change
    if (change >= 0) {
        changeElement.className = 'price-up';
    } else {
        changeElement.className = 'price-down';
    }
}

function updateStockCard(symbol, overviewData, quote) {
    const volume = formatLargeNumber(parseFloat(quote['06. volume']));
    const marketCap = formatLargeNumber(parseFloat(overviewData['MarketCapitalization']));
    const dividendYield = (parseFloat(overviewData['DividendYield']) * 100).toFixed(2) + '%';

    const stockCard = document.getElementById(`stock-card-${symbol}`);
    stockCard.innerHTML = `
        <div>Market Closed: ${quote['07. latest trading day']} ${quote['08. previous close']}</div>
        <div>Volume: ${volume}</div>
        <div>Market Capitalization: ${marketCap}</div>
        <div>Dividends Yield (FY): ${dividendYield}</div>
    `;
}

function initializeWidgets() {
    const container = document.getElementById('stock-widgets-container');
    
    for (const [name, symbol] of Object.entries(companies)) {
        const widget = createStockWidget(symbol, name);
        container.appendChild(widget);
        fetchStockData(symbol); // Fetch data for each symbol
    }

    const container1 = document.getElementById('stock-widgets-container1');
    
    for (const [name, symbol] of Object.entries(companies)) {
        const widget = createStockWidget(symbol, name);
        container1.appendChild(widget);
        fetchStockData(symbol); // Fetch data for each symbol
    }
}






initializeWidgets();
