import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vikings_scraper.settings')
django.setup()

BOT_NAME = "vikings_scraper"

SPIDER_MODULES = ["vikings_scraper.spiders"]
NEWSPIDER_MODULE = "vikings_scraper.spiders"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Paris'


from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'scrape_vikings_test': {
        'task': 'vikings_scraper.tasks.scrape_vikings',
        'schedule': crontab(minute='*/1'),  # Runs every minute for testing
    },
    'scrape_norsemen_test': {
        'task': 'vikings_scraper.tasks.scrape_norsemen',
        'schedule': crontab(minute='*/1'),  # Runs every minute for testing
    },
    'scrape_nfl_test': {
        'task': 'vikings_scraper.tasks.scrape_nfl_players',
        'schedule': crontab(minute='*/1'),  # Runs every minute for testing
    },
}

INSTALLED_APPS = [
    'django_celery_beat',
    'django_celery_results',
    'vikings_scraper',
]

DOWNLOADER_MIDDLEWARES = {
    'vikings_scraper.middlewares.SeleniumMiddleware': 800,
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0'
]

ITEM_PIPELINES = {
    'vikings_scraper.pipelines.VikingsScraperPipeline': 300,
}

SELENIUM_DRIVER_NAME = 'edge'
SELENIUM_DRIVER_EXECUTABLE_PATH = r"C:\Users\Aridon\Downloads\edgedriver_win64 (1)\msedgedriver.exe"
SELENIUM_BROWSER_EXECUTABLE_PATH = None
SELENIUM_DRIVER_ARGUMENTS = ['--headless', '--disable-gpu', '--ignore-certificate-errors']

ROBOTSTXT_OBEY = False

DEBUG = True

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



