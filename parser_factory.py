from ninenews_parser import NineNewsParser
from parser_interface import Parser

# Hardcoded Nine News, can be improved if more than one news source added.
NINE_NEWS: str = "https://www.9news.com.au/just-in"


class ParserFactory:
    """
    Static Parser Factory Class to potentially create parsers dynamically for multiple sites.
    """

    @staticmethod
    def create_parser(site_url: str) -> Parser:
        """
        Factory create for creating parsers based on the source site url. Potentially can query db for recognised sites.
        For now the sites are just hard-coded.
        :param site_url:
        :return:
        """
        if site_url == NINE_NEWS:
            return NineNewsParser(True)
        else:
            print("Error while creating parser for site", site_url)
