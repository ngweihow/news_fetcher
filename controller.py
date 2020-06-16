import requests

from bs4 import BeautifulSoup

from parser_factory import ParserFactory
from parser_interface import Parser
from connector import Connector
from typing import List


class Controller:
    def __init__(self, site_url: str, interval: int):
        self.url = site_url
        self.interval = interval

    def define_parser_for_site(self) -> Parser:
        """
        Fetch appropriate parser given the site url. Can be modified with more logic regarding multiple
        site url if supporting more sources in the future.
        :return: Appropriate Parser object.
        """
        return ParserFactory.create_parser(self.url)

    def extract_html(self) -> List[dict]:
        """
        Extract the html from site and parse it.
        :return: Extracted html in soup format.
        """
        # Getting html from url.
        response: requests.Response = requests.get(self.url)
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

        # Parsing with appropriate parser.
        news_parser: Parser = self.define_parser_for_site()
        print(soup.find("div", {"class": "story__abstract"}))
        print(news_parser.parse_html(soup))

        return news_parser.parse_html(soup)

    def news_update(self) -> None:
        # Setup of Schema.
        Connector.initialise_db()
        # Insertion of sole site.
        Connector.insert_site(self.url)

        # Extract html.
        articles: List[dict] = self.extract_html()

        # Insert articles and update latest.
        [Connector.insert_article(self.url, a) for a in articles]
        Connector.update_latest(self.url, articles[0].get("title"))



        # Connector.insert_site("google.com")
        # Connector.insert_article("google.com", {"title": "Test", "details": "details", "link": "google.com/article1"})
        print(Connector.has_article("Test2", "google.com"))
