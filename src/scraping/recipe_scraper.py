from .scraper import BaseScraper

class NYT_Scraper(BaseScraper):
    def scrape_author(self):
        self._author_name = self.scraper.find("span", class_="owner-name").text
    
    def scrape_name(self):
        self._name = self.scraper.find("h1", class_="recipe-name").text

    def scrape_ingredients(self):
        ingredients_div = self.scraper.find("div", class_="recipe-materials-div")
        for p_tag in ingredients_div.findAll("p", class_=""):
            ingredients = p_tag.find_next_sibling("ul", "recipe-materials").findAll("li")
            self._ingredients.append({p_tag.text: [ingredient.text for ingredient in ingredients]})
           
    
    def scrape_instructions(self):
        instructionList = self.scraper.find("ol", class_="recipe-instructions")
        for instruction in instructionList.findAll("li"):
            self._instructions.append(instruction.text)
    