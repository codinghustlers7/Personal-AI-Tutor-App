FROM python:3.9-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . .

# Expose the port Flask uses
EXPOSE 3000


# Start the app with Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:3000", "--workers", "3"]

