# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app and templates folder into the container
COPY calc.py .
COPY templates/ /app/templates/

# Expose the container's port 5000
EXPOSE 5000

# Command to run the app when the container starts
CMD ["python", "calc.py"]
