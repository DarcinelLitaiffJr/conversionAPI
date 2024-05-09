from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_currency_rate(base_currency, target_currency):
    # Substitua YOUR_API_KEY pela sua chave da API ExchangeRate-API
    api_key = "YOUR_API_KEY"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para respostas de erro HTTP
        
        data = response.json()
        if data['result'] == 'success':
            rate = data['conversion_rates'].get(target_currency)
            if rate is not None:
                return rate, None  # Sucesso, retorna a taxa e `None` para o erro
            else:
                return None, f"Cotação para {target_currency} não encontrada."
        else:
            return None, data.get('error-type', 'Erro desconhecido')
    except requests.RequestException as e:
        return None, f"Erro ao conectar com a ExchangeRate-API: {e}"

@app.route('/api/rate', methods=['GET'])
def rate():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    
    if not base_currency or not target_currency:
        return jsonify({'error': 'Parâmetros "base" e "target" são necessários'}), 400
    
    rate, error = get_currency_rate(base_currency, target_currency)
    
    if error:
        return jsonify({'error': error}), 500
    else:
        return jsonify({
            'base_currency': base_currency,
            'target_currency': target_currency,
            'rate': rate
        })

if __name__ == '__main__':
    app.run()
