from selenium import webdriver
from selenium.webdriver.common.by import By
from backend import soup
import time
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)

def init_bot(opt:str):
    options = webdriver.FirefoxOptions()
    if opt:
        options.add_argument("--headless")
    else:
        options.add_argument("--start-maximized")


    driver = webdriver.Firefox(options=options)
    logging.info("Initialized bot with Firefox")
    return driver

def scrape(bot, id, start, end, verbose):
    access(bot, f"https://scholar.google.co.id/citations?user={id}&hl=en")
    articles = load_all_articles(bot, start, end)
    # Sort articles by year in ascending order
    sorted_articles = sorted(articles, key=lambda x: x['year']) # type: ignore
    logging.info(f"Scraped and sorted {len(sorted_articles)} articles")
    return sorted_articles

def load_all_articles(bot, starty, endy):
    show_more_button_xpath = "//button[@id='gsc_bpf_more']"
    while True:
        try:
            # Scroll to the "Show more" button
            show_more_button = bot.find_element(By.XPATH, show_more_button_xpath)
            bot.execute_script("arguments[0].scrollIntoView(true);", show_more_button)
            # Check if the button is not disabled
            if show_more_button.get_attribute("disabled") is not None:
                logging.info("No more articles to load")
                break
            logging.info("Loading more articles...")
            # Click the "Show more" button
            show_more_button.click()
            # Wait a bit for the page to load more items
            time.sleep(2)  # Adjust sleep time as necessary
        except NoSuchElementException:
            logging.info("No 'Show more' button found, assuming all articles are loaded")
            break
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None
    page_source = bot.page_source
    articles = soup.filter_by_year(page_source, starty, endy)
    logging.info(f"Loaded {len(articles)} articles from page source")
    return articles

def access(bot, url: str):
    try:
        bot.get(url)
        logging.info(f"Accessed URL: {url}")
    except Exception as e:
        logging.error(f"Error accessing URL {url}: {e}")
        bot.quit()

def export(articles, export_dir):
    logging.info(f"Exporting {len(articles)} articles to {export_dir}")
    pass