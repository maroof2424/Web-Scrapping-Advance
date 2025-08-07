# ✅ **Week 1 – Daily Plan: `requests` + `BeautifulSoup` (Static Scraping)**

### 🗂️ Folder: `Week01_Requests_BeautifulSoup/`

---

## 📅 **Day 1: Intro to HTTP & Web Scraping**

### 🔍 Focus:

* What is web scraping?
* How the web works (URLs, HTML, HTTP methods: GET/POST)
* Inspecting web pages using browser dev tools
* Introduction to `requests` and `BeautifulSoup`

### 🧪 Practice:

* Install: `pip install requests beautifulsoup4`
* Make your first `GET` request
* Load and print HTML using BeautifulSoup

### 📁 Files:

```
day01_intro/
├── get_request_demo.py
└── parse_html_demo.py
```

---

## 📅 **Day 2: HTML Parsing & Data Extraction**

### 🔍 Focus:

* HTML tags, classes, IDs
* Use `soup.find()`, `soup.find_all()`
* Extract: `.text`, `.get("href")`, `.attrs`

### 🧪 Practice:

* Parse a saved HTML file or use a real webpage
* Extract titles, links, and descriptions from a simple page

### 📁 Files:

```
day02_parsing/
├── extract_links.py
└── extract_text.py
```

---

## 📅 **Day 3: Scrape Quotes from quotes.toscrape.com**

### 🔍 Focus:

* Practice full page scraping
* Loop through tags and collect data

### 🧪 Mini Project:

* Scrape quotes, authors, and tags from: [https://quotes.toscrape.com](https://quotes.toscrape.com)

### 📁 Files:

```
day03_quotes/
├── scrape_quotes.py
└── output_quotes.json
```

---

## 📅 **Day 4: Scrape Books from books.toscrape.com (Part 1)**

### 🔍 Focus:

* Pagination basics
* Create functions for scraping

### 🧪 Project:

* Scrape book title, price, rating from page 1

### 📁 Files:

```
day04_books/
├── books_page1.py
└── output_books.csv
```

---

## 📅 **Day 5: Handle Pagination – books.toscrape.com (Part 2)**

### 🔍 Focus:

* Loop through multiple pages
* Combine results and export to CSV

### 🧪 Project:

* Scrape all book pages (title, price, availability)

### 📁 Files:

```
day05_books_pagination/
├── scrape_all_books.py
└── all_books.csv
```

---

## 📅 **Day 6: IMDb Top 50 Scraper**

### 🔍 Focus:

* Nested tag extraction
* Handling attributes, classes

### 🧪 Mini Project:

* Scrape IMDb top 50 movies (title, rating, year)

### 📁 Files:

```
day06_imdb/
├── scrape_imdb_top50.py
└── imdb_top50.csv
```

---

## 📅 **Day 7: Review + Save to CSV/JSON + Bonus**

### 🔍 Focus:

* Use `csv` and `json` modules
* Review key concepts
* Add error handling with `try-except`
* Use functions to clean code

### 🧪 Practice:

* Convert previous scrapes to JSON and CSV
* Write reusable scraping functions

### 📁 Files:

```
day07_review/
├── save_csv_json.py
└── utils.py
```

---

## 🧰 Tools You'll Use in Week 1

| Tool            | Use                        |
| --------------- | -------------------------- |
| `requests`      | Send HTTP requests         |
| `BeautifulSoup` | Parse HTML & extract data  |
| `csv` / `json`  | Save structured data       |
| DevTools (F12)  | Inspect web page structure |

---

## Want a Python script to auto-create this Week 1 folder + files?

I can give you a generator script that will:

* Create folders: `day01_intro/`, ..., `day07_review/`
* Add starter `README.md` and empty `.py` files

