from pathlib import Path

from pathlib import Path
from corsheaders.defaults import default_headers
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'api',
    'corsheaders',
    'scraping'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    os.getenv('CORS_ALLOWED_ORIGIN')
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery settings
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/0')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Paris'

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'scrape_vikings': {
        'task': 'scraping.scraping.tasks.scrape_vikings',
        'schedule': crontab(minute='*/50'),
    },
    'scrape_norsemen': {
        'task': 'scraping.scraping.tasks.scrape_norsemen',
        'schedule': crontab(minute='*/50'),
    },
    'scrape_nfl_players': {
        'task': 'scraping.scraping.tasks.scrape_nfl_players',
        'schedule': crontab(minute='*/50'),
    }
}

BOT_NAME = 'scraping'
SPIDER_MODULES = ['scraping.scraping.spiders']
NEWSPIDER_MODULE = 'scraping.scraping.spiders'

ITEM_PIPELINES = {
    'scraping.scraping.pipelines.CombinedScraperPipeline': 300,
}

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scraping.scraping.middlewares.SeleniumMiddleware': 800,
}

USER_AGENTS = [
    os.getenv("USER_AGENT_1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"),
    os.getenv("USER_AGENT_2", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0')
]

SELENIUM_DRIVER_NAME = os.getenv('SELENIUM_DRIVER_NAME', 'chrome')
SELENIUM_BROWSER_EXECUTABLE_PATH = os.getenv('SELENIUM_BROWSER_EXECUTABLE_PATH', r"C:\Program Files\Google\Chrome\Application\chrome.exe")
SELENIUM_DRIVER_ARGUMENTS = os.getenv('SELENIUM_DRIVER_ARGUMENTS', '--headless --disable-gpu --ignore-certificate-errors').split()

ROBOTSTXT_OBEY = os.getenv('ROBOTSTXT_OBEY', 'False') == 'True'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = int(os.getenv('AUTOTHROTTLE_START_DELAY')or '5')
AUTOTHROTTLE_MAX_DELAY = int(os.getenv('AUTOTHROTTLE_MAX_DELAY') or '60')