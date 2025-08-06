# 🗓️ **6-Week Web Scraping Roadmap (Requests, BS4 → Scrapy Advanced)**

---

## ✅ **Week 1: Requests + BeautifulSoup (Static Scraping)**

### 📚 Topics:

* HTTP methods: GET, POST
* HTML structure, parsing DOM
* `requests` for page requests
* `BeautifulSoup` for parsing
* Extracting: text, links, attributes
* Pagination
* Save to CSV/JSON

### 🧪 Mini Projects:

* Scrape quotes from [quotes.toscrape.com](http://quotes.toscrape.com)
* Scrape book data from [books.toscrape.com](https://books.toscrape.com)
* Scrape top 50 IMDb movies

---

## ✅ **Week 2: Scrapy – Beginner**

### 📚 Topics:

* Install and set up Scrapy
* Scrapy project structure: items, spiders
* CSS & XPath selectors
* `parse()` function
* Output to CSV/JSON

### 🧪 Projects:

* Create a spider for `quotes.toscrape.com`
* Extract quote, author, tags
* Save in JSON

---

## ✅ **Week 3: Scrapy – Pagination & CrawlSpider**

### 📚 Topics:

* Handle pagination
* Use `CrawlSpider` and `Rule`
* Pass arguments to spiders
* Logging and debugging
* Organizing large scrapes

### 🧪 Projects:

* Scrape all products from [books.toscrape.com](https://books.toscrape.com)
* Use CrawlSpider to follow product links

---

## ✅ **Week 4: Scrapy – Pipelines, Images, Exporters**

### 📚 Topics:

* Use Item Pipelines (cleaning + validation)
* Export to CSV, JSON, MongoDB, PostgreSQL
* Download images with Scrapy
* Custom file storage pipelines

### 🧪 Projects:

* Scrape e-commerce product listings with images
* Save data and images locally or to DB

---

## ✅ **Week 5: Scrapy – Middleware, Proxies & Anti-Bot**

### 📚 Topics:

* User-agent rotation
* Proxy rotation (free or paid)
* Handle anti-bot systems
* Custom downloader middlewares
* Handle cookies, sessions

### 🧪 Projects:

* Scrape LinkedIn job posts (if possible)
* Scrape a site with bot protection using proxy pool

---

## ✅ **Week 6: Automation, Scheduling, Deployment**

### 📚 Topics:

* Automate Scrapy with cron / schedule
* Run spider from Python script
* Use `Scrapyd`, `Scrapy Cloud`, or PythonAnywhere
* Retry policies, request delays
* Logging, error handling

### 🧪 Final Projects:

* Price Tracker: Track product prices (e.g., Amazon, Daraz)
* Job Aggregator: Scrape remote jobs daily and update database
* Event Scraper: Scrape city events and notify via email/Telegram

---

# 🧰 Tools Used Throughout

| Tool                         | Use                          |
| ---------------------------- | ---------------------------- |
| `requests`                   | Basic HTTP requests          |
| `BeautifulSoup`              | HTML parsing                 |
| `Scrapy`                     | Advanced scraping & crawling |
| `csv`, `json`, `pandas`      | Save and analyze data        |
| `Selenium` (optional)        | For JS-rendered sites        |
| `MongoDB` / `PostgreSQL`     | Data storage                 |
| `Fake User-Agent`, `Proxies` | Bypass bot protections       |
| `cron` / `schedule`          | Run jobs daily               |
| `Scrapyd` / `PythonAnywhere` | Deployment                   |

---
