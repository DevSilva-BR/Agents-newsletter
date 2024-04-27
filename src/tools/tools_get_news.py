import requests
import os
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.tools import tool
from dotenv import load_dotenv


from src.utils.ignored_elements import get_ignored_elements
from src.utils.queries import queries_polity
from src.utils.format_markdown import FormatDocs
# from src.utils.blacklist import blacklist

load_dotenv()

class Tools:
    def __init__(self):
        # self.API_KEY = "baa6eff12c304cd0a001c6d5be834f1a"
        self.API_KEY = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        self.ignored_elements = get_ignored_elements()
        self.formatter = FormatDocs()
        # use queries_polity for query in list
        self.queries = ["brasil", "china", "economia"]  # Example queries

    # @tool("fetch article")
    def fetch_full_article(self, article_url):
        """Fetch the full article content from the article URL."""
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p', string=True)
            filtered_paragraphs = []
            for paragraph in paragraphs:
                if not any(paragraph.select(ignored) for ignored in self.ignored_elements):
                    filtered_paragraphs.append(paragraph.get_text())
            text_content = '\n'.join(filtered_paragraphs)
            return text_content
        else:
            return ""

    # @tool("fetch full article")
    def fetch_news(self):
        """Fetch news articles and process their contents."""
        days_ago = 1
        all_articles = []
        for query in self.queries:
            params = {
                'q': query,
                'from': (date.today() - timedelta(days=days_ago)).strftime('%Y-%m-%d'),
                'sortBy': 'publishedAt',
                'apiKey': self.API_KEY,
                'language': 'pt',
                'pageSize': 1,
            }
            response = requests.get(self.base_url, params=params)
            if response.status_code != 200:
                print(f"Error fetching news: {response.status_code} - {response.text}")
                all_articles.append("Failed to retrieve news.")
                continue

            articles = response.json().get('articles', [])
            for article in articles:
                full_content = self.fetch_full_article(article['url'])
                article['content'] = full_content
                all_articles.append(article)
                
        return all_articles


    def create_post(self):
        """
        Fetches news articles using the provided queries, formats them as Markdown content, and returns the formatted content.

        Args:
            article (dict): A dictionary representing a news article.
    
        Returns:
            str: The formatted Markdown content containing the news articles.
        """
        try:
            articles = self.fetch_news()
            markdown_content = self.formatter.format_to_markdown(articles)
            markdown_save = self.formatter.save_articles(articles)
            # markdow_save = self.formatter.load_context()
            return markdown_save
        except Exception as e:
            print(f"An error occurred: {e}")
    


result = Tools()
rr = result.create_post()
print(f"result: {rr}")