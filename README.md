# News Fetcher

Command Line tool for fetching live updates of newest information from news sites.

Written with Python3.6 with Postgresql chosen for the SQL server.

## Running application
### Postgres with Docker
Running it via mapping through localhost:5432 (port on your own local can be something else)
```
docker run -p 5432:5432 --name news -e POSTGRES_PASSWORD=password -d postgres
```

### App
Running it on provided virtual environment for python3.
```
./venv/bin/python3 main.py
```

Running it on your own virtual environment.
```
pip3 install -r requirements.txt
./venv/bin/python3 main.py
```

## Design Choices
### Technical 
- Did not use any Python frameworks to keep the application as simple and light as possible.
- Postgresql chosen as it is commonly used and the most reliable and easy to use.
- Static Factory Pattern used to increase cohesion of Parser creator.
- Parser made with Strategy Pattern to account for potential use of multiple website sources.


### Requirements
- Currently will only be able to fetch news from one source, however supports multiple sources.
- Frequency of checker checking news sources will be determined via configuration.
- Postgres started on Docker File
- Application started with provided virtual env but able to create a similar virtual env yourself with the requirements.txt.



