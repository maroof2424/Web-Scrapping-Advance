import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text , "html.parser")

heading = soup.find_all(["h1","h2","h3"])
paragraph = soup.find_all("p")

print("Heading")
for h in heading:
    print("-",h.text.strip())

print("Paragraph")
for p in paragraph:
    print("-",p.text.strip())