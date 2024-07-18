import logging
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO)

def filter_by_year(page, start, end):
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("tr", {"class": "gsc_a_tr"})
    
    if not articles:  # Check if the articles list is empty
        logging.info("No articles found.")
        return []

    filtered_articles = []

    for article in articles:
        year_text = article.find("td", {"class": "gsc_a_y"}).text
        if not year_text:
            continue
        year = int(year_text)
        if start <= year <= end:
            title = article.find("td", {"class": "gsc_a_t"}).find("a").text
            author = article.find("td", {"class": "gsc_a_t"}).find("div", {"class": "gs_gray"}).text
            article_dict = {
                "title": title,
                "author": author,
                "year": year
            }
            filtered_articles.append(article_dict)

    return filtered_articles