from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraping.scraping.settings')
app = Celery('scraping')
app.config_from_object('django.conf:settings', namespace='CELERY')

from scraping.scraping.tasks import scrape_vikings, scrape_norsemen, scrape_nfl_players

app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    worker_pool='solo',
    broker_connection_retry_on_startup=True,
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
