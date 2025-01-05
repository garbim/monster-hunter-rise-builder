# Use uma imagem base do Node.js
FROM node:18-alpine

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY package.json ./

# Instala as dependências usando Yarn
RUN npm install -g yarn && yarn install

# Copia o resto dos arquivos do projeto
COPY . .

# Compila o aplicativo para produção
RUN yarn build

# Define a porta usada pela aplicação
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["yarn", "serve"]
