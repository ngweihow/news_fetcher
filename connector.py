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

            connection.commit()
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            sys.exit(0)

    @staticmethod
    def initialise_db() -> None:
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
                           "id             SERIAL PRIMARY KEY,"
                           "url            TEXT,"
                           "last_update    TEXT"
                           ");")
            # Create News table.
            cursor.execute("CREATE TABLE IF NOT EXISTS news_sites.articles ("
                           "id      SERIAL PRIMARY KEY,"
                           "title   TEXT,"
                           "details TEXT,"
                           "url     TEXT,"
                           "site_id int REFERENCES news_sites.sites (id)"
                           ");")
            connection.commit()
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
            cursor.execute("INSERT INTO news_sites.articles (title,details ,url, site_id )"
                           "values ("
                           "%s, %s, %s, (SELECT id FROM news_sites.sites WHERE url = %s)"
                           ");",
                           (article["title"], article["details"], article["link"], site_url))

            connection.commit()
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
                           "values (%s, %s)", ("", site_url))

            connection.commit()
            cursor.close()
            connection.close()
            print("Inserted " + site_url)

        except (Exception, psycopg2.Error) as error:
            print("Error inserting site", error)
            return False

        return True

    @staticmethod
    def has_article(last_update: str, site_url: str) -> bool:
        """
        Check whether or not an article exists already in the database, hence determining if site has updated.
        :param last_update: Article Title to be checked.
        :param site_url: The news site's URL.
        :return: Boolean indicating if it is updated.
        True if the database already contains it.
        False if it is a new article.
        """
        updated: bool = False

        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()

            cursor.execute("SELECT EXISTS ("
                           "SELECT true FROM news_sites.sites WHERE url=%s and last_update=%s"
                           ");",
                           (site_url, last_update))

            updated = cursor.fetchall()[0][0]
            connection.commit()

            cursor.close()
            connection.close()
            print("Checked " + site_url + " for " + last_update)

        except (Exception, psycopg2.Error) as error:
            print("Error checking site", error)

        return updated

    @staticmethod
    def update_latest(site_url: str, latest: str) -> None:
        """
        Update the site with the latest article.
        :param site_url: The news site's URL.
        :param latest: Latest article of the site.
        :return:
        """
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="password",
            )

            cursor = connection.cursor()

            cursor.execute("UPDATE news_sites.sites "
                           "SET last_update=%s"
                           "WHERE url=%s;", (latest, site_url))

            connection.commit()
            cursor.close()
            connection.close()
            print("Updated " + site_url + " with " + latest)

        except (Exception, psycopg2.Error) as error:
            print("Error updating latest in site", error)
