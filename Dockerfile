FROM python:3.13-slim
WORKDIR /app
COPY src/transform.py src/transform.py
COPY data/input.csv data/input.csv
CMD ["python", "src/transform.py"]
