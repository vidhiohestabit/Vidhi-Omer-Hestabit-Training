# Dockerfile

FROM node:18
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all app files
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Start the app (run app.js)
CMD ["node", "app.js"]
