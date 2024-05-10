 ## API de cotação de moedas em tempo real.

## Pré-requisitos
### 🤖 Ferramentas/Tecnologias:
- Token da Exchange [Exchange Rate API](https://www.exchangerate-api.com/)
- Instale [Python3](https://www.python.org/downloads/) para Mac, Linux, ou Windows:

### Introdução:
  #### Precisa  instalar a biblioteca de requests
  ```bash
  pip install requests
  ```
  #### Precisa  instalar a Framework de Flask para yfinance, pode pser instalado separadamente.
  ```bash
  pip install Flask yfinance
  ```
### Utilizando a API
  #### Comando para executar a API
  ```bash
  python3 currency_rate.py
  ```

  #### Hoje ela tem apenas uma rota que é inserido duas moedas e ela traz o valor convertido, segue o exemplo de requisição.
  ```
  GET  http://localhost:5000/api/rate?base=BRL&target=PEN
  ```
