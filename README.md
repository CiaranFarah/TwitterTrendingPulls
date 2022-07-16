TwitterPull.py: 

To pull the Twitter Data from the API I used the Tweepy Python library (https://www.tweepy.org/). I used the latitude and longitude of Scotiabank Arena to get the WOEID (Where on Earth ID) for Canada and used that for my get trends request. I stored the trending topics in a JSON file for historical purposes. I turned the return data from the API into a Pandas Dataframe so it can easily be sent to my Azure hosted postgreSQL database in main.py.

DailySnapshot.py: 

When processing the data and making a daily snapshot I query the trending_topics table in the PostgreSQL database for everything on the current date. TwitterPull.py runs right before this so any new daily trends will be ready in the DB to be queried. I turn the returned query into a Pandas Dataframe and also into a dictionary so it can be stored as a JSON file for historical purposes. From there I use the Pandas to_string function to turn my Dataframe into a string so I can easily pass it to a text file for a quick readable daily snapshot. I create a "Twitter Daily Trends" Snapshot text file and save it locally. Like last time, I return the Dataframe so it can be sent to the database in main.py.

main.py: 

Finally, in my main script I run my Twitter Pull function and my Daily Snapshot Function. Since pulling from Twitter API requires my personal Twitter tokens, and for the database I needed my password, the passwords.txt file is not included in this Github project. This script sends the trending topics to its own table in my PostgreSQL Database, as well as a table for the daily snapshots.

I used Windows Task Scheduler (See xml file) to run my main.py every day at 1PM.
