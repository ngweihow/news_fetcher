import requests

from bs4 import BeautifulSoup

from ninenews_parser import NineNewsParser
from parser_interface import Parser
from connector import Connector

URL: str = "https://www.9news.com.au/just-in"
INTERVAL: int = 60


# set the headers as a browser

def extract_html(url: str) -> BeautifulSoup:
    """
    Extract the html from site and parse it.
    :param url: The site URL specified as a string.
    :return: Extracted html in soup format.
    """
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    news_parser: Parser = NineNewsParser(True)
    print(news_parser.parse_html(soup))

    return soup

# def init_db() -> None:



def main():
    print("Hello World!")
    extract_html(URL)
    Connector.test_db()
    Connector.initialise_db()
    print(Connector.has_article("abc", "google.com"))


if __name__ == "__main__":
    main()
