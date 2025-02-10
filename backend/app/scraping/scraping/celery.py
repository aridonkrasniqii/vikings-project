from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('scraping')
app.config_from_object(f'django.conf:settings', namespace='CELERY')
from scraping.scraping.tasks import scrape_vikings, scrape_norsemen, scrape_nfl_players
app.autodiscover_tasks()

