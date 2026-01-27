# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application when the container launches
# Default command runs the simulation with 30 stops and 3 vehicles
CMD ["python", "main.py", "--stops", "30", "--vehicles", "3"]
