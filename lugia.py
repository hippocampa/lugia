import click
from api.lugiascraper import LugiaScraper


@click.command()
@click.option("--id", help="Scrape data based on Google Scholar ID")
@click.option(
    "--file",
    help="Scrape data based on a list of Google Scholar ID from .txt File",
)
@click.option("--start", default=2020, help="Scrape year start")
@click.option("--end", default=2024, help="Scrape year end")
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
@click.option("--export-dir", help="Export directory")
@click.option("--count", is_flag=True, help="Only count the number of articles")
@click.option("--headless", is_flag=True, help="Run the scraper in headless mode", default=False)
def hello(id, file, start, end, verbose, export_dir, count, headless):
    """
    Lugia: Scraping Author's Publication Data from Google Scholar
    """
    scraper = LugiaScraper(id, file, start, end, verbose, export_dir, count, headless)
    scraper.scrape()
    scraper.quit()


if __name__ == "__main__":
    hello()
