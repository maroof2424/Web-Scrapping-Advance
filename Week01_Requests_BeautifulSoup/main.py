import os

# Root folder name
root_folder = "Week01_Requests_BeautifulSoup"

# Structure: subdir → list of files
structure = {
    "day01_intro": ["get_request_demo.py", "parse_html_demo.py"],
    "day02_parsing": ["extract_links.py", "extract_text.py"],
    "day03_quotes": ["scrape_quotes.py", "output_quotes.json"],
    "day04_books": ["books_page1.py", "output_books.csv"],
    "day05_books_pagination": ["scrape_all_books.py", "all_books.csv"],
    "day06_imdb": ["scrape_imdb_top50.py", "imdb_top50.csv"],
    "day07_review": ["save_csv_json.py", "utils.py"],
}

# Create the root folder
os.makedirs(root_folder, exist_ok=True)

# Loop through and create directories and files
for subdir, files in structure.items():
    subdir_path = os.path.join(root_folder, subdir)
    os.makedirs(subdir_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(subdir_path, file)
        with open(file_path, 'w', encoding='utf-8') as f:
            if file.endswith(".py"):
                f.write(f"# {file}\n\n")
            elif file.endswith(".json"):
                f.write("[]\n")
            elif file.endswith(".csv"):
                f.write("title,price,rating\n")

# Create README.md in root
readme_path = os.path.join(root_folder, "README.md")
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write("# Week 1: Requests + BeautifulSoup\n\n")
    f.write("This week covers static web scraping using Python's `requests` and `BeautifulSoup` libraries.\n")

print("✅ Week 1 folder structure created successfully.")
