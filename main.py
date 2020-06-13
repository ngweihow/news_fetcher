import requests

from bs4 import BeautifulSoup
import time

URL: str = "https://www.9news.com.au/just-in"


# set the headers as a browser

def extract_html(url: str) -> BeautifulSoup:
    response: requests.Response = requests.get(url)
    print(response)

    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    print(soup.find('div', {"class": "feed__stories"}).prettify())
    return soup

def main():
    print("Hello World!")
    extract_html(URL)


if __name__ == "__main__":
    main()
