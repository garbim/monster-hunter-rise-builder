FROM node:18-slim

WORKDIR /

COPY package.json ./
COPY .yarn .yarn

# Modificando esta linha para ser compatível com Yarn 3
RUN yarn install --immutable --enable-scripts

# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build

# Use a lightweight nginx image to serve the static files
FROM nginx:alpine

# Copy the built assets from builder stage
COPY --from=0 / /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]