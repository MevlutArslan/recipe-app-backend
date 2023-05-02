from .scraper import BaseScraper

class NYT_Scraper(BaseScraper):
    def scrape_author(self):
        self._author_name = self.scraper.find("span", class_="owner-name").text
    
    def scrape_name(self):
        self._name = self.scraper.find("h1", class_="recipe-name").text

    def scrape_imageUrl(self):
        img_tag = self.scraper.select_one('.recipe-single-img img')
        self._imageUrl = img_tag['src']

    def scrape_yield(self):
        self._recipeYield = self.scraper.find('span', itemprop="recipeYield").get_text().strip()

    def scrape_prepTime(self):
        self._prepTime = self.scraper.find('span', {'itemprop': 'prepTime'}).text.strip()

    def scrape_cookTime(self):
        self._cookTime = self.scraper.find('span', {'itemprop': 'cookTime'}).text.strip()
    
    def scrape_ingredients(self):
        ingredients_div = self.scraper.find("div", class_="recipe-materials-div")
        for p_tag in ingredients_div.findAll("p", class_=""):
            ingredients = p_tag.find_next_sibling("ul", "recipe-materials").findAll("li")
            self._ingredients.append({p_tag.text: [ingredient.text for ingredient in ingredients]})
           
    
    def scrape_instructions(self):
        instructionList = self.scraper.find("ol", class_="recipe-instructions")
        for instruction in instructionList.findAll("li"):
            self._instructions.append(instruction.text)
    