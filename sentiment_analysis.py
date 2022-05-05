#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 02:28:31 2022

@author: fabioribeiro
"""

import re
import json

# save the positive words into a list called p_list
with open('positive.txt') as f:
    p_txt = f.read()
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
   


# save the negative words into a list called n_list
with open('negative.txt') as f:
    n_txt = f.read()
    n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
   

# process the tweets
    
    word_list1
    word_list2 = []
    text2=[]
    for i in range(len(df_ws):
        txt2 = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', dp[i])
        word_list1 = txt2.replace('\n',' ').replace('  ',' ').lower().split(' ')
        word_list2=word_list2 + word_list1
        
    
    # create empty dictionaries
    word_count_dict = {}
    word_count_positive = {}
    word_count_negative= {}
    
    for word in word_list2:
		# count all words frequency
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
		# count if it is a positive word
        if word in p_list:
            if word in word_count_positive.keys():
                word_count_positive[word] += 1
            else:
                word_count_positive[word] = 1
		# else see if it is a negative word
        elif word in n_list:
            if word in word_count_negative.keys():
                word_count_negative[word] += 1
            else:
                word_count_negative[word] = 1
        else: # do nothing
			pass
			
    list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    list_positive = sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
    list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)

    with open('word_count.csv', 'w')as f1:
        for i in list_dict:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_positive.csv', 'w')as f1:
        for i in list_positive:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_negative.csv', 'w')as f1:
        for i in list_negative:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
            
    print("the number of negative words found in the tweets are : " +str(len(list_negative)))
    print("the number of positive words found in the tweets are : " +str(len(list_positive)))
    
    print("the 10 most redundant negative words are : ")
    for i in range(10):
        print(list_negative[i])
        
     print("the 10 most redundant positive words are : ")
     for i in range(10):
         print(list_positive[i])
