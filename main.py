from TwitterPull import twitter_pull
from DailySnapshot import create_daily_snapshot
from sqlalchemy import create_engine
from datetime import datetime

CANADA_WOEID = 23424775
current_date = datetime.today().strftime('%Y-%m-%d')
passwords_file = open("passwords.txt")
passwords = {}
# Get all info from passwords text file for security purposes
for line in passwords_file:
    equals_index = line.index("=")  # Use equal sign as delimiter
    passwords[line[:equals_index]] = line[equals_index + 1:].strip()

passwords_file.close()

trending_topics_df = twitter_pull(passwords["c_key"], passwords["c_secret"], passwords["a_token"], passwords["a_token_secret"], current_date)

engine = create_engine(passwords["postgres"])  # Using Azure Hosted PostgreSQL DB
trending_topics_df.to_sql("trending_topics", engine, if_exists="append", index=True)

daily_trending_snapshot_df = create_daily_snapshot(engine, current_date)
daily_trending_snapshot_df.to_sql("daily_snapshots", engine, if_exists="append", index=False)


