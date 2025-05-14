import os
import requests 
from src.injection.db_manager import create_news_table, insert_article
from src.config.settings import raw_data
from dotenv import load_dotenv
from src.utils.logger import get_logger 

load_dotenv()
logger = get_logger("data_fetch")

def fetch_news(query = "ai", page_size = 100, pages = 1, output_path = raw_data):
    API_KEY = os.getenv("API_KEY")
    articles = [] 

    for page in range(1, pages + 1):
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&page={page}&apiKey={API_KEY}"
        response = requests.get(url) 
        data = response.json() 

        if data.get("status") != "ok":
            logger.info(f"Error fetching page {page}: {data.get('message')}")
            break 

        logger.info(f"Fetched data from NEWSAPI on topic {query}") 
        for article in data["articles"]:
            create_news_table() 
            articles.append(article)
            insert_article(article) 
        logger.info("Inserted the articles into our database")

if __name__ == "__main__":
    fetch_news() 