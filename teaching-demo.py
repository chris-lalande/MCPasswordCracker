# json parsing demo

# Library for HTTP requests
import requests

# Constant to hold our URLs
ASSIGNED_URL = "http://172.31.29.252"
MUSIC_URL = "http://davidpots.com/jakeworry/017%20JSON%20Grouping,%20part%203/data.json"

# define the function with a url (string) argument
def parse_json(url_arg):
    response = requests.get(url=url_arg)

    music_and_books = response.json()

    print(music_and_books)

# Call the function
parse_json(MUSIC_URL)