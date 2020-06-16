from bs4 import BeautifulSoup

# File imports.
from parser_interface import Parser

from typing import List


class NineNewsParser(Parser):

    def __init__(self, cold_start: bool):
        self.cold_start = cold_start

    def parse_html(self, soup: BeautifulSoup) -> List[dict]:
        """
        Parsing the html on the nine news page.
        :param soup: HTML file in soup format.
        :return: List of dictionaries representing the articles to be placed into the database.
        """
        articles: list = []
        soup_content: BeautifulSoup = soup.find('div', {"class": "feed__stories"})
        content_list: list = soup_content.find_all('article')

        for article in content_list:
            # Adding title.
            info: dict = {"title": article.find("span", {"class": "story__headline__text"}).string}

            # Adding abstract.
            if article.find("div", {"class": "story__abstract"}).contents[0]:
                info["details"] = article.find("div", {"class": "story__abstract"}).contents[0].string

            # Link.
            if article.find("a").has_attr('href'):
                info["link"] = article.find("a")["href"]

            # Adding article to articles list.
            articles.append(info)

        return articles

    def get_last_updated(self, soup: BeautifulSoup) -> str:
        """
        Retrieve last update of site.
        :param soup: HTML file in soup format.
        :return: String title of the latest article for finding out last update.
        """
        content_list: list = soup.find_all('article')
        if len(content_list) > 0:
            return content_list[0].find("span", {"class": "story__headline__text"}).string
        else:
            return ""
