# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code
COPY . .

# Expose the Flask app port
EXPOSE 5001

# Define the entry point command
CMD [ "python", "app.py" ]
