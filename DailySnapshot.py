from datetime import datetime
import json
import os
import pandas as pd


def daily_snapshot():
    files = os.listdir("../MLSEApplicationProject")
    current_date = datetime.today().strftime('%Y-%m-%d')

    todays_snapshot_file_name = [file for file in files if file.startswith(current_date)][0]  # Cycle project directory
    # and find json file that was pulled from Twitter Pull Function, we take first instance to make this a string

    open_file = open(todays_snapshot_file_name)
    trending_topics_dict = json.load(open_file)

    trends = trending_topics_dict["trends"]
    snapshot_df = pd.DataFrame(trends)
    snapshot_df["date"] = current_date

    snapshot_df.drop(columns=["url", "promoted_content", "query"], inplace=True)  # Drop irrelevant columns for snapshot
    snapshot_df_string = snapshot_df.to_string(index=False, columns=["name", "tweet_volume"])

    file_string = "TwitterSnapshot-" + current_date
    daily_snapshot_file = open(file_string, "x")
    daily_snapshot_file.write("Twitter Daily Trending Topics in Canada\n")
    daily_snapshot_file.write(current_date + "\n")
    daily_snapshot_file.write(snapshot_df_string)

    daily_snapshot_file.close()

    return snapshot_df

