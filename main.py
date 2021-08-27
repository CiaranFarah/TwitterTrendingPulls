from TwitterPull import twitter_pull
from DailySnapshot import daily_snapshot
from sqlalchemy import create_engine

CANADA_WOEID = 23424775
c_key = "Qx9NUC17dFkPK3i6862cnRJRg"
c_secret = "r4nGh2tXsnr16WZDmDEeOxk5IZsvnDLnCpUJL0i34uVDvylhE2"
a_token = "1430584802407813120-1DHy1xPPyQvKr63Ue7y3I4o347Hmt2"
a_token_secret = "HTG9I79oBziej1K2NookkDiOEQ7WT1YLpUVGwhkI4Ry5H"

trending_topics_df = twitter_pull(c_key, c_secret, a_token, a_token_secret)

engine = create_engine("postgresql://postgres:Pokemon11!@localhost:5432/TwitterPulls")  # Using local PostgreSQL DB
trending_topics_df.to_sql("TrendingTopics", engine, if_exists="append", index=False)

daily_trending_snapshot_df = daily_snapshot()
daily_trending_snapshot_df.to_sql("DailySnapshots", engine, if_exists="append", index=False)


