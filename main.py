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

    soup_content: BeautifulSoup = soup.find('div', {"class": "feed__stories"})
    content_list: list = soup_content.find_all('article')

    for article in content_list:
        # print(str(article))
        print(article.find("span", {"class": "story__headline__text"}).string + "\n")
        if article.find("div", {"class": "story__abstract"}):
            print("Details: " + article.find("div", {"class": "story__abstract"}).string)
        if article.find("a").has_attr('href'):
            print(article.find("a")["href"])
        print("-" * 5)


    return soup

def main():
    print("Hello World!")
    extract_html(URL)


if __name__ == "__main__":
    main()
