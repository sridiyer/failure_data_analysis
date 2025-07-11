# Use Python 3.11 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8082
EXPOSE 8082

# Set the default command to run the specified Python script
CMD ["python", "tests/gr_doc_ext.py"] 