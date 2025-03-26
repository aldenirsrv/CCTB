from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS  # Importando CORS
import requests
import time

app = Flask(__name__)
CORS(app)  # Permitir CORS para todas as origens
socketio = SocketIO(app)

# URL base da API CoinGecko
BASE_URL = "https://api.coingecko.com/api/v3"

# Função para obter o preço de qualquer criptomoeda usando o crypto_id
def get_crypto_price(crypto_id):

    try:
        url = f"{BASE_URL}/simple/price?ids={crypto_id}&vs_currencies=usd"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return None

# Função para enviar o preço em tempo real via WebSocket
def send_real_time_price(crypto_id):
    while True:
        # Pega o preço da criptomoeda
        data = get_crypto_price(crypto_id)
        
        if data:
            # Envia o preço para o frontend
            socketio.emit('price_update', {'crypto_id': crypto_id, 'price': data[crypto_id]['usd']})
        else:
            print(f"Erro ao buscar preço para {crypto_id}")

        # Atraso de 1 segundo
        time.sleep(1)

# Rota para obter o preço do Bitcoin ou de qualquer criptomoeda
@app.route('/api/crypto/price/<crypto_id>', methods=['GET'])
def get_price(crypto_id):
    data = get_crypto_price(crypto_id)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to retrieve data'}), 500

# Rota para iniciar o WebSocket de preços em tempo real
@app.route('/start_price_updates/<crypto_id>', methods=['GET'])
def start_price_updates(crypto_id):
    # Inicia o envio do preço em tempo real
    socketio.start_background_task(send_real_time_price, crypto_id)
    return jsonify({"message": f"Started price updates for {crypto_id}"}), 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
