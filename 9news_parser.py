from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

# File imports.
from parser_interface import Parser


class NineNewsParser(Parser):

    def __init__(self, cold_start: bool):
        self.cold_start = cold_start

    def parse_html(self, soup: BeautifulSoup) -> dict:
        """
        Parsing the html on the nine news page.
        :param soup: HTML file in soup format.
        :return: Dictionary representing the news to be placed into the database.
        """
        soup_content: BeautifulSoup = soup.find('div', {"class": "feed__stories"})
        content_list: list = soup.find_all('article')

        for article in content_list:
            # print(str(article))
            print(article.find("span", {"class": "story__headline__text"}).string + "\n")
            if article.find("div", {"class": "story__abstract"}):
                print("Details: " + article.find("div", {"class": "story__abstract"}).string)
            if article.find("a").has_attr('href'):
                print(article.find("a")["href"])
            print("-" * 5)

        return {}