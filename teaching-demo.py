# json parsing demo

# Library for HTTP requests
import requests

# Library for JSON parsing

# Constant to hold our URLs
ASSIGNED_URL = "http://172.31.29.252"
MUSIC_URL = "http://davidpots.com/jakeworry/017%20JSON%20Grouping,%20part%203/data.json"
BOOKS_URL = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

# title to search for
title_to_search = "Fairy tales"

def parse_json(json_doc):
    if len(json_doc) == 1:
        # if we only got one object back
        # we probably have a named json object
        # get the first value and repeat the process on that
        json_doc = list(json_doc.values())[0]
        parse_json(json_doc)
    else:
        for media in json_doc:
            if media['title'] == title_to_search:
                auth = media['author']
                return auth

# define the function with a url (string) argument
def request_media(url_arg):

    #call the url (GET) and get the response
    #set the arguement into the request call
    response = requests.get(url=url_arg)

    #parse the response into a JSON document
    music_and_books = response.json()
    return parse_json(music_and_books)

    #print(music_and_books)

# Call the function with the preferred URL
author = request_media(MUSIC_URL)

if author is None:
    print("The book was not found")
else:
    print("Author: " + author)