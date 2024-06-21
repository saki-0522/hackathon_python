# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /python

# Copy the current directory contents into the container at /app
COPY . /python

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "detect.py"]

