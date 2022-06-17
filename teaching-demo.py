### json parsing demo

#Library for HTTP requests
import requests

# Constant to hold our URL
URL = "http://172.31.29.252"

response = requests.get(url=URL)

music_and_books = response.json

print(music_and_books)