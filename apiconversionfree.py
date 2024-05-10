from flask import Flask, jsonify, request
import yfinance as yf
import warnings

# Ignorar FutureWarning e outros avisos
warnings.simplefilter(action='ignore', category=FutureWarning)

app = Flask(__name__)

def get_currency_rate(base_currency, target_currency):
    # Constrói o símbolo para a cotação no formato usado pelo Yahoo Finance
    symbol = f"{base_currency}{target_currency}=X"
    
    # Obtém os dados da cotação
    data = yf.Ticker(symbol)
    
    # Tenta obter o preço atual; se não disponível, tenta o preço de fechamento do último período
    try:
        # Histórico de um dia para obter a última cotação
        hist = data.history(period="1d", interval="5m")
        if not hist.empty:
            # O último preço pode ser o preço de fechamento
            rate = hist['Close'].iloc[-1]
            return rate
        else:
            # Se não houver histórico, pode ser que a moeda não seja suportada ou o mercado esteja fechado
            return None
    except Exception as e:
        print(f"Erro ao obter a cotação: {e}")
        return None

@app.route('/api/rate', methods=['GET'])
def rate():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    
    if not base_currency or not target_currency:
        return jsonify({'error': 'Parâmetros "base" e "target" são necessários'}), 400
    
    rate = get_currency_rate(base_currency, target_currency)
    if rate is not None:
        return jsonify({
            'base_currency': base_currency,
            'target_currency': target_currency,
            'rate': rate
        })
    else:
        return jsonify({'error': 'Não foi possível obter a cotação.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
