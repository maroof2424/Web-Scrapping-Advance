import requests
from bs4 import BeautifulSoup
import json 

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

quotes_data=[]

for qoute in soup.find_all("div",class_="quote"):
    text = qoute.find("span",class_="text").text.strip()
    author = qoute.find("small",class_="author").text.strip()
    tags = [tag.text for tag in qoute.find_all("a",class_="tag")]

    quotes_data.append({
        "text":text,
        "author":author,
        "tags":tags
    })

with open("output_quotes.json","w",encoding="utf-8") as f:
    json.dump(quotes_data,f,indent=4,ensure_ascii=False)

print(f"✅ Scraped {len(quotes_data)} quotes and saved to output_quotes.json")