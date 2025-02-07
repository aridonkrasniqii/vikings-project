FROM python:3.12-slim

ENV VIRTUAL_ENV=/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app_container

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app_container/
RUN pip install --no-cache-dir -r /app_container/requirements.txt

COPY . /app_container/

EXPOSE 8000
