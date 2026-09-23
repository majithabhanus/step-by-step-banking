FROM python:3.13-slim

WORKDIR /app

# Update available OS security fixes
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .

# Install only application dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip uninstall -y setuptools wheel || true

# Copy application
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]