from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import random
import os
import time
from binance.client import Client
from threading import Thread

app = Flask(__name__)

# Get API keys from environment variables
api_key = os.getenv("KEY_BINANCE")
secret_key = os.getenv("SECRET_BINANCE")

# Initialize the Binance client
cliente_binance = Client(api_key, secret_key)

# Enable CORS for React (localhost:3001)
CORS(app, origins=["*"])

# Initialize SocketIO with WebSocket support
socketio = SocketIO(app, cors_allowed_origins="*", transports=["websocket"])

def gen_random_num():
    return random.uniform(50, 300)

# Function to get the price of any cryptocurrency using the crypto_id
def get_crypto_price():
    try:
        # Get prices from Binance
        btc = cliente_binance.get_ticker(symbol="BTCUSDT")
        eth = cliente_binance.get_ticker(symbol="ETHUSDT")
        xrp = cliente_binance.get_ticker(symbol="XRPUSDT")
        sol = cliente_binance.get_ticker(symbol="SOLUSDT")
        mkr = cliente_binance.get_ticker(symbol="MKRUSDT")

        # Prepare response
        return {
            'timestamp': time.time(),
            'btc': {
                'price': btc['lastPrice'],
                'crypto_id': btc['symbol'],
                'crypto_name': 'Bitcoin',
                'img': 'https://cryptologos.cc/logos/bitcoin-btc-logo.png?v=040',
                'data': {
                    'percent': btc['priceChangePercent'],
                    'close_price': btc['prevClosePrice'],
                    'lastPrice': btc['lastPrice'],
                    'openPrice': btc['openPrice'],
                    'tradeCount': btc['count']
                }
            },
            'eth': {
                'price': eth['lastPrice'],
                'crypto_id': eth['symbol'],
                'crypto_name': 'Ethereum',
                'img': 'https://cryptologos.cc/logos/ethereum-eth-logo.png?v=040',
                'data': {
                    'percent': eth['priceChangePercent'],
                    'close_price': eth['prevClosePrice'],
                    'lastPrice': eth['lastPrice'],
                    'openPrice': eth['openPrice'],
                    'tradeCount': eth['count']
                }
            },
            'xrp': {
                'price': xrp['lastPrice'],
                'crypto_id': xrp['symbol'],
                'crypto_name': 'XRP',
                'img': 'https://cryptologos.cc/logos/xrp-xrp-logo.png?v=040',
                'data': {
                    'percent': xrp['priceChangePercent'],
                    'close_price': xrp['prevClosePrice'],
                    'lastPrice': xrp['lastPrice'],
                    'openPrice': xrp['openPrice'],
                    'tradeCount': xrp['count']
                }
            },
            'sol': {
                'price': sol['lastPrice'],
                'crypto_id': sol['symbol'],
                'crypto_name': 'Solano',
                'img': 'https://cryptologos.cc/logos/solana-sol-logo.png?v=040',
                'data': {
                    'percent': sol['priceChangePercent'],
                    'close_price': sol['prevClosePrice'],
                    'lastPrice': sol['lastPrice'],
                    'openPrice': sol['openPrice'],
                    'tradeCount': sol['count']
                }
            },
            'mkr': {
                'price': mkr['lastPrice'],
                'crypto_id': mkr['symbol'],
                'crypto_name': 'Maker Price',
                'img': 'https://cryptologos.cc/logos/maker-mkr-logo.png?v=040',
                'data': {
                    'percent': mkr['priceChangePercent'],
                    'close_price': mkr['prevClosePrice'],
                    'lastPrice': mkr['lastPrice'],
                    'openPrice': mkr['openPrice'],
                    'tradeCount': mkr['count']
                }
            },
            'selling': {
                'labels': [btc['symbol'], eth['symbol'], xrp['symbol'], sol['symbol'], mkr['symbol']],
                'data': [btc['count'], eth['count'], xrp['count'], sol['count'], mkr['count']]
            }
        }
    except Exception as e:
        print(f"Error fetching crypto prices: {e}")
        return None

# Function to send real-time price updates via WebSocket
def send_real_time_price():
    while True:
        data = get_crypto_price()
        if data:
            socketio.emit('price_update', data)
        else:
            print("Error fetching price")
        time.sleep(10)

@app.route('/api/static', methods=['GET'])
def get_price():
    try:
        data = get_crypto_price()
        if data:
            return jsonify(data)
        else:
            return jsonify({'error': 'Failed to retrieve data'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Health check endpoint
@app.route('/healthz')
def health_check():
    return "OK", 200  # HTTP status code 200 means the service is healthy

# Function to simulate Bitcoin data every second (for testing purposes)
def emit_bitcoin_data_simulation():
    while True:
        bitcoin_data = {
            'timestamp': time.time(),
            'price': random.uniform(50000, 60000),  # Random price between 50k and 60k USD
            'currency': 'USD'
        }
        socketio.emit('bitcoin_data', bitcoin_data)
        time.sleep(1)

@app.route('/')
def index():
    return "Flask server is running!"

if __name__ == '__main__':
    # "In applications that need to perform tasks asynchronously or in parallel (such as processing real-time data, making background requests, etc.),
    #  using threads allows the send_real_time_price function to run in parallel without blocking the execution of the rest of the code.
    # "Start the thread to send real-time prices
    thread = Thread(target=send_real_time_price)
    thread.start()

    # Start Flask-SocketIO server to listen on all interfaces (for Docker or external access)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)