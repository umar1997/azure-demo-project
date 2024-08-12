FROM ubuntu:22.04

ARG HOME=/app
ENV HOME=${HOME}

USER root

RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    inetutils-ping \
    lsb-release \
    curl \
    sudo \
    vim \
    lsof \
    screen \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    telnet \
    && apt-get autoremove -yqq --purge && apt-get clean
                

RUN apt-get install python3 \
    python3-dev \
    python3-pip \
    python3-venv -y

RUN pip install --upgrade pip

COPY ./demoApp/requirements.txt ${HOME}/requirements.txt
RUN pip install -r ${HOME}/requirements.txt


COPY ./demoApp/ ${HOME}/
WORKDIR ${HOME}