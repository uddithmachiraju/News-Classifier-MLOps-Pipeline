from pathlib import Path 

# Raw data path 
raw_data = Path("data/raw/news.csv") 
raw_data.parent.mkdir(parents = True, exist_ok = True) 