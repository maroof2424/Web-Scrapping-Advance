## 📅 **Day 1: Intro to HTTP & Web Scraping**

---

### 🔍 **Focus Topics**

* ✅ What is Web Scraping?
* ✅ How the web works (URLs, HTTP, HTML)
* ✅ HTTP Methods: GET and POST
* ✅ Inspect elements using browser DevTools (F12)
* ✅ Introduction to `requests` and `BeautifulSoup`

---

### 🧪 **Practice Tasks**

1. ✅ Install the required libraries:

   ```bash
   pip install requests beautifulsoup4
   ```
2. ✅ Make your first GET request to a webpage
3. ✅ Load and print HTML using BeautifulSoup

---

### 📁 **Directory + Files**

```
Week01_Requests_BeautifulSoup/
└── day01_intro/
    ├── get_request_demo.py
    └── parse_html_demo.py
```

---

### 🐍 **File 1: `get_request_demo.py`**

```python
# get_request_demo.py

import requests

url = "https://httpbin.org/get"  # Example URL for testing GET request
response = requests.get(url)

# Status code check
print(f"Status Code: {response.status_code}")

# Raw text content
print("Response Body:")
print(response.text)
```

---

### 🐍 **File 2: `parse_html_demo.py`**

```python
# parse_html_demo.py

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Print entire HTML
print("Full HTML of the page:")
print(soup.prettify())

# Extract page title
title = soup.title.string
print("\nPage Title:", title)
```

---

### 💡 Tips for Today:

* Always check the HTTP status code (200 = OK).
* Use `.text` for response content.
* `soup.prettify()` = clean indented HTML.
* `.title.string`, `.find()`, `.find_all()` will be used from Day 2.

