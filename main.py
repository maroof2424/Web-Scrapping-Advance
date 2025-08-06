import os

# Define your weekly structure
weeks = [
    ("Week01_Requests_BeautifulSoup", "Requests + BeautifulSoup (Static Scraping)"),
    ("Week02_Scrapy_Beginner", "Scrapy – Beginner"),
    ("Week03_Scrapy_CrawlSpider", "Scrapy – Pagination & CrawlSpider"),
    ("Week04_Scrapy_Pipelines", "Scrapy – Pipelines, Images, Exporters"),
    ("Week05_Scrapy_Proxies", "Scrapy – Middleware, Proxies & Anti-Bot"),
    ("Week06_Scrapy_Deploy", "Automation, Scheduling, Deployment"),
]

# Base directory
base_path = os.path.abspath(".")

for folder_name, description in weeks:
    dir_path = os.path.join(base_path, folder_name)
    os.makedirs(dir_path, exist_ok=True)

    readme_path = os.path.join(dir_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# 📚 {folder_name}\n\n")
        f.write(f"**Week Topic:** {description}\n\n")
        f.write("## 📝 Notes:\n\n- \n\n")
        f.write("## 🧪 Mini Projects:\n\n- \n")

print("✅ All week folders and README.md files created.")
