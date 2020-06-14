import sys

import psycopg2


class Connector:

    @staticmethod
    def test_db() -> None:
        """
        Test the database connection.
        :return: None
        """
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
            print(connection.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            sys.exit(0)

    @staticmethod
    def initialise_db(self) -> None:
        """
        Initialise the database Schema and add Tables.
        :return: None
        """
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()
            # Create Schema.
            cursor.execute("CREATE SCHEMA IF NOT EXISTS news_sites;")
            # Create Sites table.
            cursor.execute("CREATE TABLE IF NOT EXISTS news_sites.sites ("
                           "id             SERIAL PRIMARY KEY"
                           "url            TEXT,"
                           "last_update    TEXT"
                           ");")
            # Create News table.
            cursor.execute("CREATE TABLE IF NOT EXISTS news_sites.articles ("
                           "id      SERIAL PRIMARY KEY,"
                           "title   TEXT,"
                           "details TEXT,"
                           "url     TEXT,"
                           "site_id SERIAL,"
                           "FOREIGN KEY (sites) REFERENCES news_sites.sites (id)"
                           ");")
            cursor.close()
            connection.close()
            print("Database Successfully initiated.")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            sys.exit(0)

    @staticmethod
    def insert_article(site_url: str, article: dict) -> bool:
        """
        Insert the article into the database given its site url and article dictionary.
        :param site_url: URL of the news site source.
        :param article: Article contents extracted from the soup.
        :return: Boolean indicating success of adding article.
        """
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()
            # Adding the article contents.
            cursor.execute("WITH linked_site_id AS ("
                           "SELECT id FROM news_sites.sites WHERE url = '%s'"
                           ")"
                           "INSERT INTO news_sites.articles (title,details ,url, site_id )"
                           "values ("
                           "'%s', '%s', '%s', (SELECT linked_site_id.id FROM linked_site_id)"
                           ");",
                           site_url, article["title"], article["details"], article["link"])

            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

        except (Exception, psycopg2.Error) as error:
            print("Error inserting article", error)
            return False

        return True

    @staticmethod
    def insert_site(site_url: str) -> bool:
        """
        Insert Site given url and set last_updated to empty string.
        :param site_url: URL of the news site source.
        :return: Boolean indicating success of adding source.
        """
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()

            cursor.execute("INSERT INTO news_sites.sites (last_update, url)"
                           "values ('%s', '%s')", "", site_url)

            cursor.close()
            connection.close()
            print("Inserted " + site_url)

        except (Exception, psycopg2.Error) as error:
            print("Error inserting site", error)
            return False

        return True
