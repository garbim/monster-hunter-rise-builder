FROM node:18-alpine

# Define o diretório de trabalho
WORKDIR /app

# Instala Python e cria um link simbólico para garantir que python3 funcione
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python

# Copia os arquivos necessários
COPY package.json ./

# Instala o Yarn e as dependências
RUN yarn install

# Copia o restante dos arquivos do projeto
COPY . .

# Compila o aplicativo para produção
RUN yarn build

# Define a porta usada pela aplicação
EXPOSE 8080

# Comando para iniciar o servidor Python na interface 0.0.0.0 e porta 8080
CMD ["python3", "-m", "http.server", "8080", "--bind", "0.0.0.0", "--directory", "./dist"]
