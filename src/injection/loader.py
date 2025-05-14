import pandas as pd
from src.utils.logger import get_logger
from src.config.settings import raw_data
from src.injection.fetch_data import fetch_news
from src.injection.db_manager import connect_db 

logger = get_logger("data_loading")

def load_articles():
    fetch_news() 
    with connect_db() as conn:
        logger.info("Loading the data from database")
        df = pd.read_sql("SELECT * FROM news_articles", conn) 
        df.to_csv(raw_data, index = False) 
        logger.info(f"Saved the loaded data into a Pandas Datafram in {raw_data}")

if __name__ == "__main__":
    load_articles()