FROM centos

LABEL maintainer="Namal K (https://github.com/namalk)"

RUN dnf install -y python38; pip3 install --no-cache-dir fastapi; pip3 install --no-cache-dir uvicorn
RUN mkdir /app
COPY ./app /app

ENV TZ=Australia/Sydney
WORKDIR /app
