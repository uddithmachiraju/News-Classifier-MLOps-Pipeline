from pathlib import Path 

# Raw data path 
raw_data = Path("data/raw/news.csv") 
raw_data.parent.mkdir(parents = True, exist_ok = True) 

# data base path 
db_path = Path("data/db/news.db") 
db_path.parent.mkdir(parents = True, exist_ok = True) 