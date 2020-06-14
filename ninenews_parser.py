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
        info: dict = {}
        soup_content: BeautifulSoup = soup.find('div', {"class": "feed__stories"})
        content_list: list = soup_content.find_all('article')

        for article in content_list:
            # Adding title.
            info["title"] = article.find("span", {"class": "story__headline__text"}).string

            # Adding abstract.
            if article.find("div", {"class": "story__abstract"}):
                info["details"]: article.find("div", {"class": "story__abstract"}).string

            # Link.
            if article.find("a").has_attr('href'):
                info["link"] = article.find("a")["href"]

        return info

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
