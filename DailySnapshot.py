import json
import pandas as pd
import sqlalchemy


def create_daily_snapshot(db_engine, current_date):
    query_string = "SELECT * FROM trending_topics WHERE date = '"+current_date+"'"  # Need quatations around date since postgres can't recognize it is a string and not a date format

    daily_snapshot_df = pd.read_sql(sqlalchemy.text(query_string), db_engine)
    daily_snapshot_df.rename(columns={"index": "trend_rank"}, inplace=True)  # Renamed for clarity

    daily_snapshot_df.drop(columns=["url", "promoted_content", "query"], inplace=True)

    json_string = "TwitterSnapshot-" + current_date + ".json"

    daily_trends_dict = daily_snapshot_df.to_dict()  # Change DF to dictionary so it can easily be stored as JSON

    with open(json_string, "w") as file:
        json.dump(daily_trends_dict, file, indent=4)  # Indent for readability

    snapshot_df_string = daily_snapshot_df.to_string(index=False, columns=["name", "tweet_volume"]) # Save as text file as well for quick readability
    file_string = "TwitterSnapshot-" + current_date + ".txt"
    daily_snapshot_file = open(file_string, "w")
    daily_snapshot_file.write("Twitter Daily Trending Topics in Canada\n")
    daily_snapshot_file.write(current_date + "\n")
    daily_snapshot_file.write(snapshot_df_string)

    daily_snapshot_file.close()

    return daily_snapshot_df





