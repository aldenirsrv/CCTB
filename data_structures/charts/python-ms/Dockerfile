# Usar a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências (requirements.txt)
COPY requirements.txt .

# Instalar as dependências no contêiner
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . .

# Expor a porta que a aplicação vai rodar (ajuste conforme sua aplicação)
EXPOSE 5000

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]