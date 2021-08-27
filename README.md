# Twitter Trending Topics for MLSE Application

Hello MLSE Data Science/Eng + Software Engineering Teams!

This is my completed case study for my Data Engineer application.

To pull the Twitter Data from the API I used the Tweepy Python library (https://www.tweepy.org/). I used the latitude and longitude of Scotiabank Arena to get the WOEID (Where on Earth ID) for Canada and used that for my get trends request. I stored the trending topics in a JSON file for historical purposes. I turned the return data from the API into a dictionary and return it as a Pandas Dataframe so it can easily be sent to my local postgreSQL database later.

When processing the data and making a daily snapshot I open the JSON file that was created from the API pull and turn it into a Pandas Dataframe. From there I use the Pandas to_string function to turn my Dataframe into a string so I can easily pass it to a text file. I create a "Twitter Daily Trends" Snapshot text file and save it locally. Like last time, I return the Dataframe so it can be sent to the database later.

Finally, in my main script I run my Twitter Pull function and my Daily Snapshot Function. Since pulling from Twitter API requires my personal Twitter tokens and for the database I needed my password, the passwords.txt file is not included in this Github project. This script sends the trending topics to its own table in my locally hosted PostgreSQL Database, as well as a table for the daily snapshots.
