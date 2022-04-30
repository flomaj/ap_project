#import packages

import tweepy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify

#set access keys

consumer_key = 
consumer_secret_key = 

access = 
access_secret = 

bearer_token = 

#configure client

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key, access_token=access, access_token_secret=access_secret)

#Finding the datas

queries = ["Bitcoin", "Ethereum","BNB", "AVAX", "LUNA", "Solana", "XRP", "Cardano", "DOT"]
data = pd.DataFrame()
for q in queries:
    tweets = client.get_recent_tweets_count(query=q, granularity="hour")
    nb_tweets_day = pd.DataFrame(tweets.data)
    data[q] = nb_tweets_day["tweet_count"].astype(int)
    
#Compute the hourly changes (%)

last_2_complete = data.iloc[-3:-1]
df = last_2_complete.T
df.columns = ["previous" , "actual"]

actual = df["actual"]
previous = df["previous"]
change = (actual - previous) / previous 

#Draw our hourly heatmap

    #Define the sizes of each crypto for the last entire hour
    
val = df["actual"].tolist()

    #set colors depending on hourly changes

color = []
for i in range(len(change)):
    if  change[i] > 0:
        color.append("green")
    if  change[i] < 0:
        color.append("red")
    if  change[i] == 0:
        color.append("grey")
        
    #Draw the heatmap
plt.figure(figsize=(8,6))
squarify.plot(sizes=val, label=queries, pad=True, color=color)
plt.axis("off")
plt.show()

#Draw a chart with the different hourly changes in %

plt.figure(figsize=(8,6))
plt.bar(queries, change, color = color, edgecolor = "black")
plt.axhline(y=0, color="black", linewidth = 5)
plt.ylabel('Social Trend Change (%)')
plt.show()

#plot the evolution of the last 24 hours

evol = data[-25:-1]
plt.figure(figsize=(8,6))
plt.plot(evol)

plt.legend(queries)

plt.ylabel('Number of Tweets ')
plt.title('Hourly Evolution of the number of Tweets (24h)')
plt.gca().get_xaxis().set_visible(False)

plt.show()