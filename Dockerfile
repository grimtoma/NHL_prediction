# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Add the current directory contents into the container at /app
ADD . /app

# Set the environment variable LD_LIBRARY_PATH to /usr/lib/wsl/lib/
ENV LD_LIBRARY_PATH=/usr/lib/wsl/lib/

# Run test_directML.py when the container launches
CMD ["python", "test_directML.py"]