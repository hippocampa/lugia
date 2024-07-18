# Lugia: The Ultimate Google Scholar Article Scraper

**Note:** This project is still underway, with more features coming soon!

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview
Welcome to **Lugia**, your new favorite companion for diving into the depths of Google Scholar! With Lugia, you can effortlessly extract article information from Google Scholar profiles using just a simple ID and date range. Whether you're a researcher, a student, or just curious about someone's academic contributions, Lugia has got you covered.

## Features
- **Easy Peasy Scraping**: Just provide a Google Scholar ID, and Lugia will fetch article titles, authors, publication dates, and citation counts for you.
- **Date Range Filtering**: Specify a start year and end year to filter articles within a specific time frame.

## Requirements
- Python 3.7+
- `selenium`
- `beautifulsoup4`
- `pandas`
- `tabulate`
- (optional) `dotenv` for environment variable management

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/lugia.git
    cd lugia
    ```
2. Install Pipenv if you haven't already:
    ```bash
    pip install pipenv
    ```
3. Install dependencies using Pipenv:
    ```bash
    pipenv install
    ```
4. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

## Usage
Run the scraper with a specific Google Scholar ID and date range:

```bash
Usage: lugia.py [OPTIONS]

  Lugia: Scraping Author's Publication Data from Google Scholar

Options:
  --id TEXT          Scrape data based on Google Scholar ID
  --file TEXT        Scrape data based on a list of Google Scholar ID from
                     .txt File
  --start INTEGER    Scrape year start
  --end INTEGER      Scrape year end
  --verbose          Will print verbose messages.
  --export-dir TEXT  Export directory
  --count            Only count the number of articles
  --headless         Run the scraper in headless mode
  --help             Show this message and exit.
```

## Output
Right now, lugia is only capable of printing all the articles in a tabular form from your terminal. Improvements are coming soon!

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the existing style and includes tests for any new functionality.

## Contact
For any questions or suggestions, please open an issue on GitHub or contact [me](mailto:tsdhrm@outlook.com).
