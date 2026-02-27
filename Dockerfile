# Usa uma imagem oficial do Python, versão enxuta
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código do projeto
COPY . .

# Comando padrão ao rodar o container (pode ser sobrescrito)
ENTRYPOINT ["python", "main.py"]