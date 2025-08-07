import requests

from bs4 import BeautifulSoup

urls = "https://wmomiti.com/"
response = requests.get(urls)

soup = BeautifulSoup(response.text,"html.parser")

print("Full Html of he page: ")
print(soup.prettify())


title = soup.title.string
print(f"Page Tile: {title}")