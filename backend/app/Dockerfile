FROM python:3.12-slim

ENV VIRTUAL_ENV=/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y \
    unzip \
    build-essential \
    libpq-dev \
    wget \
    curl \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libasound2 \
    libx11-xcb1 \
    libdbus-1-3 \
    libxtst6 \
    libxcomposite1 \
    libxdamage1 \
    libatspi2.0-0 \
    gnupg2 \
    ca-certificates \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libu2f-udev \
    libvulkan1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Download Google Chrome (version 113.0.5672.126-1)
RUN wget --no-verbose -O /tmp/chrome.deb https://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_113.0.5672.126-1_amd64.deb && \
    apt install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb

# Download latest ChromeDriver
RUN LATEST_DRIVER=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q https://chromedriver.storage.googleapis.com/${LATEST_DRIVER}/chromedriver_linux64.zip -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

WORKDIR /app_container

COPY requirements.txt /app_container/
RUN pip install --no-cache-dir -r /app_container/requirements.txt

COPY . /app_container/

EXPOSE 8000
