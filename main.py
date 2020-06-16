from controller import Controller

URL: str = "https://www.9news.com.au/just-in"
INTERVAL: int = 60


# set the headers as a browser

# def extract_html(url: str) -> BeautifulSoup:
#     """
#     Extract the html from site and parse it.
#     :param url: The site URL specified as a string.
#     :return: Extracted html in soup format.
#     """
#     response: requests.Response = requests.get(url)
#     soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
#     news_parser: Parser = NineNewsParser(True)
#     print(news_parser.parse_html(soup))
#
#     return soup

def get_config() -> None:
    return


def main():
    print("Starting News Fetcher...")
    controller: Controller = Controller(URL, INTERVAL)
    controller.news_update()

if __name__ == "__main__":
    main()
