# Usar a imagem base do Python
FROM python:3.10-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação para o contêiner
COPY . .

# Expor a porta que a aplicação irá utilizar
EXPOSE 5000

# Comando para iniciar a aplicação Flask usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "apiconversionfree:app"]
