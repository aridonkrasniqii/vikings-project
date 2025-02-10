import subprocess
from scraping.scraping.celery import app
import django
django.setup()

def run_spider(spider_name):
    command = f'scrapy crawl {spider_name}'
    process = subprocess.Popen(command, shell=True)
    process.communicate()

@app.task
def scrape_vikings(*args, **kwargs):
    print('Scraping Vikings')
    run_spider('vikings')

@app.task
def scrape_norsemen(*args, **kwargs):
    print('Scraping Norsemen')
    run_spider('norsemen')

@app.task
def scrape_nfl_players(*args, **kwargs):
    print('Scraping NFL Players')
    run_spider('nflplayers')
