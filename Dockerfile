# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy local code to the container
COPY test-server.py .
COPY requirements.txt .

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make sure we use the Uvicorn workers for production for better performance 
CMD ["uvicorn", "test-server.py:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
