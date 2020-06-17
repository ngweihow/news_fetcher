from controller import Controller
import config

"""
Main Entry to application. Grabs config and initialises Controller. 
"""


def main():
    print("Starting News Fetcher...\n")
    print("Listening on", config.URL, "\n")
    controller: Controller = Controller(config.URL, config.INTERVAL)
    controller.news_update()


if __name__ == "__main__":
    main()
