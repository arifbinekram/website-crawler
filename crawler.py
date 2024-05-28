#!/usr/bin/python3

import requests
import re
from urllib.parse import urlparse, urljoin

target_url = "https://www.vulnhub.com/"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    return re.findall(r'(?:href=")(.*?)"', response.text)

def crawl(url):
    href_links = extract_links_from(url)

    for link in href_links:
        link = urljoin(url, link)

        if "#" in link:    # # refers to original page so avoid duplicate page again and again
            link = link.split("#")[0]

        if target_url in link and link not in target_links:  # to avoid repeating the same url
            target_links.append(link)
            print("[+]urls --->", link)
            crawl(link)  # recursively crawling

crawl(target_url)
