FROM ubuntu:20.04

RUN apt-get update && apt-get install python3-pip -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP /app/main
EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]