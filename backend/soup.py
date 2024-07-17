
from bs4 import BeautifulSoup

def filter_by_year(page, start, end):
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("tr", {"class": "gsc_a_tr"})
    filtered_articles = []

    for article in articles:
        year_text = article.find("td", {"class": "gsc_a_y"}).text
        # Skip the article if the year is an empty string
        if not year_text:
            continue
        year = int(year_text)
        if start <= year <= end:
            # Assuming the structure of the article allows for extracting title and author
            title = article.find("td", {"class": "gsc_a_t"}).find("a").text
            author = article.find("td", {"class": "gsc_a_t"}).find("div", {"class": "gs_gray"}).text
            # Create a dictionary for the article
            article_dict = {
                "title": title,
                "author": author,
                "year": year
            }
            filtered_articles.append(article_dict)

    return filtered_articles