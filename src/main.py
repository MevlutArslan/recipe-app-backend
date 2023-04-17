from fastapi import FastAPI
from scraping.recipe_scraper import NYT_Scraper

app = FastAPI()

scraper = NYT_Scraper("https://www.nefisyemektarifleri.com/video/patates-puresinde-tavuk-sote/")
scraper.scrape()

@app.get("/")
def index():
    return "HELLO WORLD!"

