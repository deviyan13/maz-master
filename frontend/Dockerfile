# Use the official Node image from the Docker Hub
FROM node:14

# Set the working directory in the container
WORKDIR /src

# Copy package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the project code into the container
COPY . .

# Build the React app for production
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Serve the React app
CMD ["npm", "run", "start"]
