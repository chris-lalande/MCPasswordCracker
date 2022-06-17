# json parsing demo

# Library for HTTP requests
import requests

# Constant to hold our URL
URL = "http://172.31.29.252"
MUSIC_URL = "http://davidpots.com/jakeworry/017%20JSON%20Grouping,%20part%203/data.json"

response = requests.get(url=MUSIC_URL)

music_and_books = response.json()

print(music_and_books)
