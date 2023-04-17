from bs4 import BeautifulSoup
import requests
class BaseScraper:
    def __init__(self, url):
        self.url = url
        self._name: str
        self._author_name: str
        self._ingredients = []
        self._instructions = []
        self.scraper: BeautifulSoup
    
    def get_html(self):
        print("Getting HTML for {}".format(self.url))
        html = requests.get(self.url).text
        self.scraper = BeautifulSoup(html, features="html.parser")

    def scrape(self):
        self.get_html()
        self.scrape_author()
        self.scrape_name()
        self.scrape_ingredients()
        self.scrape_instructions()
    
    def scrape_author(self):
        raise NotImplementedError
    
    def scrape_name():
        raise NotImplementedError
    
    def scrape_ingredients(self):
        raise NotImplementedError
    
    def scrape_instructions(self):
        raise NotImplementedError