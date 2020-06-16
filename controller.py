import requests

from bs4 import BeautifulSoup

from parser_factory import ParserFactory
from parser_interface import Parser
from connector import Connector


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

    def extract_html(self) -> BeautifulSoup:
        """
        Extract the html from site and parse it.
        :return: Extracted html in soup format.
        """
        response: requests.Response = requests.get(self.url)
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        news_parser: Parser = self.define_parser_for_site()
        print(news_parser.parse_html(soup))

        return soup

    def news_update(self) -> None:
        print("Hello World!")
        self.extract_html()
        Connector.test_db()
        Connector.initialise_db()
        print(Connector.has_article("Test", "google.com"))
