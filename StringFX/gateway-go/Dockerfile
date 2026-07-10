# Use an official lightweight Go image
FROM golang:1.21-alpine AS builder

WORKDIR /build

# Initialize a go module dynamically
RUN go mod init stringfx/gateway

# Copy the source code
COPY main.go .

# Build a highly optimized, compiled binary execution file
RUN CGO_ENABLED=0 GOOS=linux go build -o gateway main.go

# Final ultra-slim deployment stage
FROM alpine:3.18
WORKDIR /app
COPY --from=builder /build/gateway .

EXPOSE 8080
CMD ["./gateway"]