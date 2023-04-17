from fastapi import FastAPI
from scraping.recipe_scraper import NYT_Scraper
from models.author import Author
from models.recipe import Recipe
from db import session
from fastapi.encoders import jsonable_encoder
import time

app = FastAPI()

def scape_and_save(url: str):
    nyt_scraper = NYT_Scraper(url)
    nyt_scraper.scrape()

    author = Author(name= nyt_scraper._author_name)
    if not session.query(Author).filter_by(name= author.name).first():
        session.add(author)
        session.commit() # need to call commit to generate the id for it.
    else:
        author = session.query(Author).filter_by(name= author.name).first()

    recipe = Recipe(name= nyt_scraper._name, author_id= author.id, ingredients= nyt_scraper._ingredients, instructions= nyt_scraper._instructions)
    session.add(recipe)
    session.commit()

with open('recipes.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        # every line is a url from nefisyemektarifleri.com
        scape_and_save(line)
        time.sleep(10)

@app.get("/")
def index():
    return "HELLO WORLD!"

@app.get("/recipe")
def get_recipe_by_id():
    recipes = session.query(Recipe).all()
    return jsonable_encoder(recipes)

@app.get("recipe/{recipe_id}")
def get_recipe_by_id(recipe_id):
    recipe = session.query(Recipe).filter_by(id= recipe_id).first()
    return jsonable_encoder(recipe)