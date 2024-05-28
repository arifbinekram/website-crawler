import requests
import re
from urllib.parse import urlparse, urljoin

# Prompt the user for the target URL
target_url = input("Enter the target URL: ").strip()

# Ensure the URL has a scheme
if not target_url.startswith(('http://', 'https://')):
    target_url = 'http://' + target_url

target_links = []

def extract_links_from(url):
    try:
        response = requests.get(url)
        print("Status code:", response.status_code)
        # Extract all links from the HTML content using regular expressions
        links = re.findall(r'href=["\'](.*?)["\']', response.text)
        print("Links found:", links)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

# Start crawling from the provided target URL
crawl(target_url)

