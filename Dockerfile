FROM python:3.9-slim
WORKDIR /app
COPY caesar.py .
CMD ["python", "caesar.py"]