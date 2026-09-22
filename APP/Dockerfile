FROM python:3.13-slim

WORKDIR /app

# Update OS packages with available security fixes
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies
COPY requirements.txt .

# Upgrade Python packaging tools and install dependencies
RUN python -m pip install --no-cache-dir --upgrade pip setuptools \
    && python -m pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]