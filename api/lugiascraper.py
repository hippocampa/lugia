import logging
from backend import bot
from tabulate import tabulate
import sys
import datetime
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LugiaScraper:
    def __init__(self, id, file, start, end, verbose, export_dir, count, headless):
        self.id = id
        self.file = file
        self.start = start
        self.end = end
        self.verbose = verbose
        self.export_dir = export_dir
        self.count = count
        self.headless = headless

    def scrape(self):
        if self.id:
            self.scrape_by_id()
        elif self.file:
            self.scrape_by_file()
        elif self.id and self.file:
            logging.warning("Please provide either Google Scholar ID or .txt File. Use --help for more information.")
            sys.exit(1)
        elif not self.id and not self.file:
            logging.warning("Please provide either Google Scholar ID or .txt File. Use --help for more information.")
            sys.exit(1)

    def scrape_by_id(self):
        logging.info(f"Scraping data based on Google Scholar ID: {self.id}")
        self.bot = bot.init_bot(opt=self.headless)
        articles = bot.scrape(self.bot, self.id, self.start, self.end, self.verbose)
        if self.verbose and self.count:
            temp = {"id": self.id, "total_articles": len(articles)}
            print(tabulate([temp], headers="keys", tablefmt="pretty"))
        if self.verbose and not self.count:
            print(tabulate(articles, headers="keys", tablefmt="pretty"))
        logging.info(f"Total articles found: {len(articles)}")

    def scrape_by_file(self):
        all_articles = []
        logging.info("Scraping data based on a list of Google Scholar IDs from .txt File: {}".format(self.file))
        self.bot = bot.init_bot(opt=self.headless)
        ids = self.get_ids_from_file()
        for id in ids:
            articles = bot.scrape(self.bot, id, self.start, self.end, self.verbose)
            if self.count:
                temp = {"id": id, "total_articles": len(articles)}
                all_articles.append(temp)
            else:
                all_articles.extend(articles)
        if self.verbose:
            print(tabulate(all_articles, headers="keys", tablefmt="pretty"))
        else:
            logging.info(f"Total articles found: {len(all_articles)}")
        self.articles = all_articles
        if self.export_dir:
            self.export_to_xlsx()

    def get_ids_from_file(self):
        with open(self.file) as f:
            ids = [line.strip() for line in f.readlines()]
        logging.info(f"Loaded {len(ids)} IDs from file")
        return ids
    
    def quit(self):
        self.bot.quit()
        logging.info("Bot quit successfully.")
    
    def export_to_xlsx(self):
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".xlsx"
        logging.info(f"Exporting data to {filename}")
        df = pd.DataFrame(self.articles)
        df.to_excel(self.export_dir + filename, index=False)
        logging.info("Export successful.")

        