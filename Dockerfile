# Python Based Docker
FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /tbot
WORKDIR /tbot
COPY start.sh /start.sh

# Running TECHNOUSERBOT
CMD ["/bin/bash", "/start.sh"]
