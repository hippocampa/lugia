from backend import bot


class LugiaScraper:
    def __init__(self, id, file, start, end):
        self.id = id
        self.file = file
        self.start = start
        self.end = end

    def scrape(self):
        if self.id:
            self.scrape_by_id()
        elif self.file:
            self.scrape_by_file()
        elif self.id and self.file:
            print("Please provide either Google Scholar ID or .txt File")
            print("Use --help for more information")
        elif not self.id and not self.file:
            print("Please provide either Google Scholar ID or .txt File")
            print("Use --help for more information")

    def scrape_by_id(self):
        print(f"Scraping data based on Google Scholar ID: {self.id}")
        self.bot = bot.init_bot()
        bot.scrape(self.bot, self.id, self.start, self.end)

    def scrape_by_file(self):
        print(
            "Scraping data based on a list of Google Scholar ID"
            + f" from .txt File: {self.file}"
        )
