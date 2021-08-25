from urllib.parse import quote
from fastapi import FastAPI
from scraper import Scrap

app = FastAPI()
quotes = Scrap()

# quotes.scrapData('life') # example


@app.get("/{category}")
async def read_item(category):
    return quotes.scrapData(category)
