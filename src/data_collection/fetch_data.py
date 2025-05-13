import os
import requests 
import pandas as pd 
from src.config import raw_data
from dotenv import load_dotenv

load_dotenv()

def fetch_news(query = "ai", page_size = 100, pages = 1, output_path = raw_data):
    API_KEY = os.getenv("API_KEY")
    articles = [] 

    for page in range(1, pages + 1):
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={page_size}&page={page}&apiKey={API_KEY}"
        response = requests.get(url) 
        data = response.json() 

        if data.get("status") != "ok":
            print(f"Error fetching page {page}: {data.get('message')}")
            break 

        articles += data["articles"]

    df = pd.DataFrame(
        [
            {
                "title": a["title"],
                "description": a["description"],
                "content": a["content"],
                "source": a["source"]["name"]
            }
            for a in articles
        ]
    )
    df.to_csv(output_path, index = False) 
    print(f"saved {len(df)} articles to {output_path}") 

if __name__ == "__main__":
    fetch_news() 