FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/install Flask==3.1.2 msgpack==1.2.1


FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /install /usr/local/lib/python3.13/site-packages

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]