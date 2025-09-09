# Usar uma imagem base leve do Python
FROM python:3.10-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para instalar as dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código-fonte para o diretório de trabalho
COPY . .

# Expor a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
