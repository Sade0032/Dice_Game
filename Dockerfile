# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY Sade0032Assignment4.py .

# Command to run the application
CMD ["python", "Sade0032Assignment4.py"]
