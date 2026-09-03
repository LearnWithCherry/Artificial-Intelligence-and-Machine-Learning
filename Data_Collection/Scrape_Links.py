import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://example.com"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a", href=True):
    text = link.get_text(" ", strip=True)
    href = urljoin(url, link["href"])

    print(text, "->", href)
