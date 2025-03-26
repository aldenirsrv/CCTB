# Use an official Golang image as the base image
FROM golang:1.15

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files into the container
COPY . .

# Ensure Go Modules is enabled
ENV GO111MODULE=on

# Run 'go mod tidy' to ensure dependencies are fetched
# Make sure the Go version in your 'go.mod' is valid (e.g., 1.15, 1.16, 1.17)
RUN go mod tidy

# Compile the Go application
RUN go build -o app .

# Expose the port your app will use (optional)
EXPOSE 8000

# Define the command to run your Go application
CMD ["./app"]