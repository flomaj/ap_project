 #import packages

import tweepy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

#ask the user for the desired coin

query = str(input("Enter the coin you are interested in..."))



#compute the hourly change of the number of Tweets

#set access keys

consumer_key = 
consumer_secret_key = 

access = 
access_secret = 

bearer_token = 

#configure client

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key, access_token=access, access_token_secret=access_secret)

#find the data

tweets = client.get_recent_tweets_count(query=query, granularity="hour")
nb_tweets_day = pd.DataFrame(tweets.data)
data = nb_tweets_day["tweet_count"].astype(int)

#find the hourly change

last_2_complete = data.iloc[-3:-1]
tw_change = (last_2_complete.iloc[1] - last_2_complete.iloc[0]) / last_2_complete.iloc[0] 

#compute the hourly change of the Google Trends Score

#find the data on Google Trends

word = [str(query)]
pytrends = TrendReq(hl='en-US', tz=120)
pytrends.build_payload(word, cat=0, timeframe='now 7-d')
data = pytrends.interest_over_time()

#find the hourly change

last_2_complete = data.iloc[-3:-1,:-1]
gt_change = (last_2_complete.iloc[1] - last_2_complete.iloc[0]) / last_2_complete.iloc[0] #*100
gt_change = gt_change[0]



#compute the indicators

#define the "trend"

if tw_change < -0.4:
    tw_status = "Very Low"
elif -0.4 <= tw_change < -0.1:
    tw_status = "Low"
elif -0.1 <= tw_change < 0.1:
    tw_status = "Neutral"
elif 0.1 <= tw_change < 0.4:
    tw_status = "Strong"
elif tw_change >= 0.4:
    tw_status = "Very Strong"
if gt_change < -0.4:
    gt_status = "Very Low"
elif -0.4 <= gt_change < -0.1:
    gt_status = "Low
elif -0.1 <= gt_change < 0.1:
    gt_status = "Neutral"
elif 0.1 <= gt_change < 0.4:
    gt_status = "Strong
elif gt_change >= 0.4:
    gt_status = "Very Strong"
    
# transform the data

if tw_change < -1:
    tw_change = -1
if tw_change > 1:
    tw_change = 1  

tw_change_n = (tw_change/2) + 0.5

if gt_change < -1:
    gt_change = -1
if gt_change > 1:
    gt_change = 1

gt_change_n = (gt_change/2) + 0.5

# Twitter Indicator

#set values
val = [(1-tw_change_n), tw_change_n]

# color & half pie chart
val.append(sum(val)) #add the half pie that will be white
colors = ['red', 'green', 'white'] #set to colour of the second half of the pie to white

# plot
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(1,1,1)
ax.pie(val, colors=colors)
ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
plt.text(0, 1.1, "Twitter Engagement", fontsize=13, weight = 300, ha = "center", wrap=True)
plt.text(-0.85, -0.2, "0", fontsize=15, weight = 700, wrap=True)
plt.text(0.78, -0.2, "1", fontsize=15, weight = 700, wrap=True)
plt.axhline(y=0, color="black", linewidth = 5)
plt.text(0, 0.2, tw_status, fontsize=17, weight = 700, ha = "center", wrap=True)
fig.show()

# Google Trends Indicator

# set values
val = [(1-gt_change_n), gt_change_n]

# color & half pie chart
val.append(sum(val)) #add the half pie that will be white
colors = ['red', 'green', 'white'] #set to colour of the second half of the pie to white

# plot
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(1,1,1)
ax.pie(val, colors=colors)
ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
plt.text(0, 1.1, "Google Engagement", fontsize=13, weight = 300, ha = "center", wrap=True)
plt.text(-0.85, -0.2, "0", fontsize=15, weight = 700, wrap=True)
plt.text(0.78, -0.2, "1", fontsize=15, weight = 700, wrap=True)
plt.axhline(y=0, color="black", linewidth = 5)
plt.text(0, 0.2, gt_status, fontsize=17, weight = 700, ha = "center", wrap=True)
fig.show()

# Merged Indicator

# set values
score = (0.5 * gt_change_n) + (0.5 * tw_change_n)
val = [(1-score), score]

# color & half pie chart
val.append(sum(val)) #add the half pie that will be white
colors = ['red', 'green', 'white'] #set to colour of the second half of the pie to white

# plot
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(1,1,1)
ax.pie(val, colors=colors)
ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
plt.text(0, 1.1, "Engagement", fontsize=13, weight = 300, ha = "center", wrap=True)
plt.text(-0.85, -0.2, "0", fontsize=15, weight = 700, wrap=True)
plt.text(0.78, -0.2, "1", fontsize=15, weight = 700, wrap=True)
plt.axhline(y=0, color="black", linewidth = 5)
plt.text(0, 0.2, gt_status, fontsize=17, weight = 700, ha = "center", wrap=True)
fig.show()