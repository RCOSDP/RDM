FROM node:20.14.0-bookworm
WORKDIR /app
COPY package*.json ./
RUN npm ci
EXPOSE 3000
CMD ["sleep", "infinity"]
