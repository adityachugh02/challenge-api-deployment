FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY /app /app
WORKDIR /app
COPY requirements.txt requirements.txt
COPY /start.sh /start.sh
RUN pip3 install -r requirements.txt
RUN chmod +x /start.sh
CMD ["/start.sh"]