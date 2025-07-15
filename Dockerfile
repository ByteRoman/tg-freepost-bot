# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set environment variables from .env file
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "bot.py"]
