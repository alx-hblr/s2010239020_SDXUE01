# Use the Golang 1.19 base image
FROM golang:1.19 AS builder

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the src directory to the container's /app directory
COPY src/ .

# Download and install dependencies for the project
RUN go get -d -v ./...

# Compile the Go code and build the binary executable file named /main
RUN go build -o /main .

# Use a minimalist base image to reduce container size
FROM debian:bullseye-slim

# Set the working directory to /app
WORKDIR /app

# Copy the binary executable from the builder image to this image
COPY --from=builder /main /app/main

# Set the binary executable as the entry point for the container
ENTRYPOINT ["/app/main"]

# Specify the default command to run when the container starts
CMD ["serve"]
