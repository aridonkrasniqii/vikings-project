import os
import sys
import django
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping.scraping.settings')
django.setup()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'api'
]

BOT_NAME = 'scraping'
SPIDER_MODULES = ['scraping.scraping.spiders']
NEWSPIDER_MODULE = 'scraping.scraping.spiders'

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'scraping.middlewares.SeleniumMiddleware': 800,
}

USER_AGENTS = [
    os.getenv("USER_AGENT_1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"),
    os.getenv("USER_AGENT_2", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0')
]

SELENIUM_DRIVER_NAME = os.getenv('SELENIUM_DRIVER_NAME', 'edge')
SELENIUM_DRIVER_EXECUTABLE_PATH = os.getenv('SELENIUM_DRIVER_EXECUTABLE_PATH', r"C:\Users\Aridon\Downloads\edgedriver_win64 (1)\msedgedriver.exe")
SELENIUM_BROWSER_EXECUTABLE_PATH = os.getenv('SELENIUM_BROWSER_EXECUTABLE_PATH', None)
SELENIUM_DRIVER_ARGUMENTS = os.getenv('SELENIUM_DRIVER_ARGUMENTS', '--headless --disable-gpu --ignore-certificate-errors').split()

ROBOTSTXT_OBEY = os.getenv('ROBOTSTXT_OBEY', 'False') == 'True'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = int(os.getenv('AUTOTHROTTLE_START_DELAY')or '5')
AUTOTHROTTLE_MAX_DELAY = int(os.getenv('AUTOTHROTTLE_MAX_DELAY') or '60')
