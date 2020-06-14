from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class Parser:
    """
    Parser Interface class to correctly parse the information from websites. Each Parser would be unique to
    their respective sources.
    """

    @abstractmethod
    def parse_html(self, soup: BeautifulSoup) -> dict:
        """
        Parsing the HTML received to a dictionary format, suitable for storing in the database.
        :param soup: HTML file in soup format.
        :return: Dictionary representing the news to be placed into the database.
        """
        return {}

    @abstractmethod
    def get_last_updated(self, soup: BeautifulSoup) -> str:
        """
        Retrieve last update of site.
        :param soup: HTML file in soup format.
        :return: String title of the latest article for finding out last update.
        """
        return ""
