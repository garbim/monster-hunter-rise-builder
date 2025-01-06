# Dockerfile.build
FROM node:18-alpine as build
WORKDIR /app
# Instalar Python 3 e pip
RUN apk add --no-cache python3 py3-pip && \
    ln -sf python3 /usr/bin/python

# Instalar bibliotecas Python necessárias
RUN python3 -m pip install --no-cache-dir requests beautifulsoup4

# Copia toda a pasta dev_script
COPY dev_scripts ./dev_scripts
RUN python3 dev_scripts/mhrb/kiranico_scrape/kiranico_scrape.py && \
    python3 dev_scripts/mhrb/kiranico_scrape/process_downloaded_data.py

# Dockerfile
FROM node:18-alpine
WORKDIR /app

# Instala Python
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python

# Copia os dados processados do estágio anterior
COPY --from=build /app/data ./data

# Copia e instala dependências
COPY package.json ./
RUN yarn install

# Copia o restante dos arquivos
COPY . .

# Build da aplicação
RUN yarn build

# Configuração do servidor
EXPOSE 8080
CMD ["python3", "-m", "http.server", "8080", "--bind", "0.0.0.0", "--directory", "./dist"]