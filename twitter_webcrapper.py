#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 01:18:05 2022

@author: fabioribeiro
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Bitcoin until:2022-05-01 since:2022-04-30" #put here what you want to webscrapp
tweets = []
limit = 5000 #how many tweets you wanna webscrap


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

