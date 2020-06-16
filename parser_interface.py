from abc import abstractmethod
from bs4 import BeautifulSoup
from typing import List


class Parser:
    """
    Parser Interface class to correctly parse the information from websites. Each Parser would be unique to
    their respective sources.
    """

    @abstractmethod
    def parse_html(self, soup: BeautifulSoup) -> List[dict]:
        """
        Parsing the HTML received to a dictionary format, suitable for storing in the database.
        :param soup: HTML file in soup format.
        :return: List of dictionaries representing the articles to be placed into the database.
        """
        return []

    @abstractmethod
    def get_last_updated(self, soup: BeautifulSoup) -> str:
        """
        Retrieve last update of site.
        :param soup: HTML file in soup format.
        :return: String title of the latest article for finding out last update.
        """
        return ""
