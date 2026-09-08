FROM node:20-slim
WORKDIR /app
# Ensure curl/essential tools if needed
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]