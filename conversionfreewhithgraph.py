import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def obter_cotacao_dolar():
    # Obter dados históricos da cotação do dólar
    start_date = datetime.now() - timedelta(days=365)  # 1 anos atrás
    end_date = datetime.now()

    df = yf.download('USDBRL=X', start=start_date, end=end_date)
    
    return df

def criar_grafico(df, periodo_meses):
    # Criar gráfico de cotação do dólar
    plt.figure(figsize=(10, 24))
    plt.plot(df['Close'], label='Cotação do Dólar (USD to BRL)')

    # Destacar mínimo e máximo
    destacar_min_max(df)

    plt.title(f'Cotação do Dólar - Últimos {periodo_meses} meses')
    plt.xlabel('Data')
    plt.ylabel('Cotação do Dólar (BRL)')
    plt.legend()
    plt.grid(True)
    plt.show()

def destacar_min_max(df):
    # Identificar índices dos valores mínimo e máximo
    indice_min = df['Close'].idxmin()
    indice_max = df['Close'].idxmax()

    # Obter valores correspondentes
    valor_min = df.loc[indice_min, 'Close']
    valor_max = df.loc[indice_max, 'Close']

    # Adicionar anotações ao gráfico
    plt.annotate(f'Min: {valor_min:.2f}', xy=(indice_min, valor_min), xytext=(indice_min, valor_min + 0.1),
                 arrowprops=dict(facecolor='red', shrink=0.05), color='red')

    plt.annotate(f'Max: {valor_max:.2f}', xy=(indice_max, valor_max), xytext=(indice_max, valor_max - 0.1),
                 arrowprops=dict(facecolor='green', shrink=0.05), color='green')


def main():
    # Obter dados
    df = obter_cotacao_dolar()

    # Criar gráfico a cada 6 meses
    periodo_meses = 24
    for i in range(0, len(df), periodo_meses * 21):  # Aproximadamente 21 dias úteis por mês
        criar_grafico(df[i:i+periodo_meses*21], periodo_meses)

if __name__ == "__main__":
    main()
