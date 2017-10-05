# Pull base image.
FROM ubuntu:16.04

# Install.
RUN \
  apt-get -y update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common

RUN \
  apt-get install -y gcc libzbar-dev python-pip && \
  rm -rf /var/lib/apt/lists/* && \
  pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

ENV LANG C.UTF-8

# Run main.py when the container launches
CMD ["python", "main.py"]
