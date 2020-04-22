FROM python:slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update
RUN apt install -y gcc postgresql-server-dev-all musl-dev
RUN rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install -r requirements.txt --no-cache-dir
EXPOSE 3000

