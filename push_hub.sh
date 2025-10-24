#!/bin/bash
echo "=== Pushing to Docker Hub ==="
DOCKER_USERNAME=varvarablaginina

docker tag caesar-cipher-app:latest $DOCKER_USERNAME/caesar-cipher-app:latest

docker push $DOCKER_USERNAME/caesar-cipher-app:latest

echo "Image pushed to Docker Hub!"
echo "Pull with: docker pull $DOCKER_USERNAME/caesar-cipher-app:latest"