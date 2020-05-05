FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

LABEL maintainer="Dariush"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

COPY ./ /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]