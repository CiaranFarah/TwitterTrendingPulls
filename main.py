from TwitterPull import twitter_pull
from DailySnapshot import daily_snapshot
from sqlalchemy import create_engine

passwords_file = open("passwords.txt")
passwords = {}
# Get all info from passwords text file for security purposes
for line in passwords_file:
    equals_index = line.index("=")
    passwords[line[:equals_index]] = line[equals_index + 1:].strip()

passwords_file.close()

trending_topics_df = twitter_pull(passwords["c_key"], passwords["c_secret"], passwords["a_token"], passwords["a_token_secret"])

engine = create_engine(passwords["postgres"])  # Using local PostgreSQL DB
trending_topics_df.to_sql("TrendingTopics", engine, if_exists="append", index=False)

daily_trending_snapshot_df = daily_snapshot()
daily_trending_snapshot_df.to_sql("DailySnapshots", engine, if_exists="append", index=False)


