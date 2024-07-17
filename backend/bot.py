from selenium import webdriver
from selenium.webdriver.common.by import By
from backend import soup
import time
from selenium.common.exceptions import NoSuchElementException
from tabulate import tabulate

def init_bot():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)
    return driver



def scrape(bot, id, start, end):
    access(bot, f"https://scholar.google.co.id/citations?user={id}&hl=en")
    articles = load_all_articles(bot, start, end)
    # Sort articles by year in ascending order
    sorted_articles = sorted(articles, key=lambda x: x['year']) # type: ignore
    print(tabulate(sorted_articles, headers="keys", tablefmt="pretty"))  # type: ignore
    # Print total number of items in the list
    print(f"Total articles: {len(sorted_articles)}")
    bot.quit()



def load_all_articles(bot, starty, endy):
    show_more_button_xpath = "//button[@id='gsc_bpf_more']"
    while True:
        try:
            # Scroll to the "Show more" button
            show_more_button = bot.find_element(By.XPATH, show_more_button_xpath)
            bot.execute_script("arguments[0].scrollIntoView(true);", show_more_button)

            # Check if the button is not disabled
          
            if show_more_button.get_attribute("disabled") is not None:
                break
            print("Loading more articles...")

            # Click the "Show more" button
            show_more_button.click()

            # Wait a bit for the page to load more items
            time.sleep(2)  # Adjust sleep time as necessary
        except NoSuchElementException:
            # If the button is not found, break the loop
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    print("Done loading all articles")
    page_source = bot.page_source
    
    # Assuming soup.filter_by_year is a function you've defined elsewhere
    return soup.filter_by_year(page_source, starty, endy)


def access(bot, url: str):
    try:
        bot.get(url)
    except Exception as e:
        print(f"Error: {e}")
        bot.quit()
