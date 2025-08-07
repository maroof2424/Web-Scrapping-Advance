## 📅 **Day 2: HTML Parsing & Data Extraction**

---

### 🔍 **Focus Topics**

* ✅ Understand HTML structure (tags, class, id)
* ✅ Using `soup.find()`, `soup.find_all()`
* ✅ Extracting:

  * `.text`: Get tag text
  * `.get("href")`: Get link URLs
  * `.attrs`: Get all tag attributes

---

### 🧪 **Practice Tasks**

* Use a simple webpage (e.g., `https://example.com`) or saved HTML
* Extract:

  * All links (`<a>`)
  * All headings (`<h1>`, `<h2>`, etc.)
  * Paragraph texts

---

### 📁 **Directory + Files**

```
Week01_Requests_BeautifulSoup/
└── day02_parsing/
    ├── extract_links.py
    └── extract_text.py
```

---

### 🐍 **File 1: `extract_links.py`**

```python
# extract_links.py

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all <a> tags
links = soup.find_all("a")

print("🔗 All Links on the Page:\n")
for link in links:
    text = link.text.strip()
    href = link.get("href")
    print(f"Text: {text or 'No Text'} | Link: {href}")
```

---

### 🐍 **File 2: `extract_text.py`**

```python
# extract_text.py

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print all headings and paragraphs
headings = soup.find_all(["h1", "h2", "h3"])
paragraphs = soup.find_all("p")

print("📌 Headings:")
for h in headings:
    print("-", h.text.strip())

print("\n📝 Paragraphs:")
for p in paragraphs:
    print("-", p.text.strip())
```

---

### 💡 Notes:

| Concept        | Example Code         |
| -------------- | -------------------- |
| Find first tag | `soup.find("a")`     |
| Find all tags  | `soup.find_all("a")` |
| Get tag text   | `tag.text.strip()`   |
| Get attribute  | `tag.get("href")`    |
| All attributes | `tag.attrs`          |

---

