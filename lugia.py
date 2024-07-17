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
def hello(id, file, start, end):
    """Simple program that greets NAME for a total of COUNT times."""
    scraper = LugiaScraper(id, file, start, end)
    scraper.scrape()


if __name__ == "__main__":
    hello()
