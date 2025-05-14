import sqlite3
from src.config.settings import db_path 
from src.utils.logger import get_logger

logger = get_logger("database") 

logger.info("Initilized the database connection")
def connect_db():
    return sqlite3.connect(db_path) 

def create_news_table():
    with connect_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS news_articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                content TEXT,
                source TEXT,
                url TEXT,
                publishedAt TEXT,
                fetchedAt TEXT DEFAULT CURRENT_TIMESTAMP)
            """
        )

def insert_article(article):
    with connect_db() as conn:
        conn.execute(
            """
            INSERT OR IGNORE INTO news_articles 
            (title, description, content, source, url, publishedAt) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                article["title"],
                article["description"],
                article["content"],
                article["source"]["name"],
                article["url"],
                article["publishedAt"]
            )
        )