import time

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

        return news_parser.parse_html(soup)

    def news_update(self) -> None:
        """
        Main entry point into application, initiates the news update process.
        """

        # Setup of Schema.
        Connector.initialise_db()
        # Insertion of sole site.
        Connector.insert_site(self.url)

        while True:
            # Extract html.
            articles: List[dict] = self.extract_html()

            # Insert articles if not found.
            for article in articles:
                if not Connector.has_article(article["title"], self.url):
                    Connector.insert_article(self.url, article)
                    self.print_article(article)
                else:
                    break

            # Remember latest article.
            article_title: str = articles[0].get("title")
            Connector.update_latest(self.url, article_title)

            # Sleep.
            print("Listening for updates...")
            time.sleep(self.interval)

    def print_article(self, article: dict) -> None:
        """
        Prints single article upon update.
        :param article:
        :return:
        """
        print("TITLE:", article["title"])
        print("Details:", article["details"])
        print("\n", article["link"])
        print("-" * 10)
