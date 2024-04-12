FROM node:alpine
WORKDIR /app

# Copy package.json
COPY package.json /app
RUN npm install

# Copy the rest of the files
COPY . /app

# Expose the port
EXPOSE 3000

# Start the app
CMD ["npm", "run", "dev"]
