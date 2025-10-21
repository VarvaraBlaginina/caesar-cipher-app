#!/bin/bash
echo "Building Docker image..."
docker build -t caesar-cipher-app:latest .
echo "Build completed!"