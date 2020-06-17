from controller import Controller

URL: str = "https://www.9news.com.au/just-in"
INTERVAL: int = 60


def get_config() -> None:
    return


def main():
    print("Starting News Fetcher...\n")
    print("Listening on", URL, "\n")
    controller: Controller = Controller(URL, INTERVAL)
    controller.news_update()


if __name__ == "__main__":
    main()
