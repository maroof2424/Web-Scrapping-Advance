import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/page-1.html"

def get_book_from_page(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for article in soup.select(".product_pod"):
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text  # .text added
        rating_class = article.p["class"][1]

        books.append({
            "title": title,
            "price": price,
            "rating": rating_class,
        })
    return books

def save_to_csv(books, filename):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "rating"])
        writer.writeheader()
        writer.writerows(books)  # writerows instead of writerow

if __name__ == "__main__":
    book_data = get_book_from_page(url)
    save_to_csv(book_data, "output_books.csv")
    print(f"Data saved in output_books.csv with {len(book_data)} books")
