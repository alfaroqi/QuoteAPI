from urllib.parse import quote
from fastapi import FastAPI
from scraper import Scrap

app = FastAPI()
quotes = Scrap()

formatData = quotes.formatData




# quotes.scrapData('life') # example


@app.get("/{category}")
async def read_item(category):
    return quotes.scrapData(category)


@app.get("/api/v1/{category}")
async def read_item(category):
    return formatData(quotes.scrapData(category))



