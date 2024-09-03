
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from pymongo import MongoClient
import time

class WebCrawler:
    def __init__(self, base_url, db_client):
        self.base_url = base_url
        self.visited_urls = set()
        self.db = db_client["crawler_database"]
        self.robot_parser = RobotFileParser()
        self.robot_parser.set_url(f"{base_url}/robots.txt")
        self.robot_parser.read()

    def can_fetch(self, url):
        return self.robot_parser.can_fetch("*", url)

    def fetch_content(self, url):
        if url in self.visited_urls or not self.can_fetch(url):
            return None
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            self.visited_urls.add(url)
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_content(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        return text.strip()

    def store_content(self, url, text):
        self.db.content.insert_one({"url": url, "text": text})

    def update_targets(self):
        # Fetch updated keywords from the database set by the classifier
        keywords = self.db.keywords.find()
        for keyword in keywords:
            search_url = f"{self.base_url}/search?q={keyword['keyword']}"
            content = self.fetch_content(search_url)
            if content:
                text = self.parse_content(content)
                self.store_content(search_url, text)
                print(f"Processed and stored content for keyword: {keyword['keyword']}")
            time.sleep(1)  # Respectful crawling by pausing between requests

# Setup MongoDB client and initialize crawler
client = MongoClient("mongodb://localhost:27017/")
crawler = WebCrawler("https://example.com", client)
