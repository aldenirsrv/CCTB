 # Use an official node image as a parent image
 FROM node:16 AS build

 # Set the working directory inside the container
 WORKDIR /app

 # Copy package.json and package-lock.json
 COPY package*.json ./

 # Install app dependencies
 RUN npm install

 # Copy all project files to the container
 COPY . .

 # Build the app
 RUN npm run build

 # Use a lighter image for the server
 FROM nginx:alpine

 # Copy the build output to the Nginx default directory
 COPY --from=build /app/build /usr/share/nginx/html

 # Expose port 80
 EXPOSE 80

 # Start Nginx
 CMD ["nginx", "-g", "daemon off;"]