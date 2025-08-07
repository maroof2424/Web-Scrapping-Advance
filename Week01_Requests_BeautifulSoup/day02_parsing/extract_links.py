import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

links = soup.find_all("a")

for link in links:
    text = link.text.strip()
    href = link.get("href")
    print(f"Text: {text or 'No text'} | Link: {url}{href}")


