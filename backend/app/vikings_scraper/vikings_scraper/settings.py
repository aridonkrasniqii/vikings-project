import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vikings_scraper.settings')
django.setup()

BOT_NAME = "vikings_scraper"

SPIDER_MODULES = ["vikings_scraper.spiders"]
NEWSPIDER_MODULE = "vikings_scraper.spiders"

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'scrape_vikings_daily': {
        'task': 'viking_app.tasks.scrape_vikings',
        'schedule': crontab(hour=0, minute=0),
    },
    'scrape_norsemen_daily': {
        'task': 'viking_app.tasks.scrape_norsemen',
        'schedule': crontab(hour=1, minute=0),
    },
    'scrape_nfl_daily': {
        'task': 'viking_app.tasks.scrape_nfl',
        'schedule': crontab(hour=2, minute=0),
    },
}

INSTALLED_APPS = [
    'django_celery_beat',
]


DOWNLOADER_MIDDLEWARES = {
    'vikings_scraper.middlewares.SeleniumMiddleware': 800,
}

SELENIUM_DRIVER_NAME = 'edge'
SELENIUM_DRIVER_EXECUTABLE_PATH = r"C:\Users\Aridon\Downloads\edgedriver_win64 (1)\msedgedriver.exe"
SELENIUM_BROWSER_EXECUTABLE_PATH = None
SELENIUM_DRIVER_ARGUMENTS = []

ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
