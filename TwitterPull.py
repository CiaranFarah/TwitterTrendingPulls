import tweepy
import json
import pandas as pd


def twitter_pull(consumer_key, consumer_secret, access_token, access_token_secret, current_date):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    lat = 43.6435  # I used the lat + long of Scotiabank Arena
    long = -79.3791

    canadian_trends_info = api.trends_closest(lat, long)
    trends_dict = canadian_trends_info[0]

    canada_woeid = trends_dict["parentid"]
    #exclusions = "hashtags"  # Trending topics has some hashtags included as well. If we don't want them pass this
    exclusions = ""

    try:  # Error handling in case I put wrong lat & long
        canadian_trending_topics = api.trends_place(canada_woeid, exclusions)
    except tweepy.TweepError:
        print("No trending topics for WOEID: {}".format(canada_woeid))

    trending_topics_dict = canadian_trending_topics[0]  # trends_place returns a list with 1 dictionary object

    json_string =  "CanadianTrendingTwitterTopics" + current_date + ".json"  # Making file name for json

    with open(json_string, "w") as file:
        json.dump(trending_topics_dict, file, indent=4)  # Indent for readability

    trends_df = pd.DataFrame(trending_topics_dict["trends"])
    trends_df["date"] = current_date  # Add date to dataframe for entry into database

    return trends_df
