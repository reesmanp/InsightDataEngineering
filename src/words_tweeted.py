# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:24:21 2015

@author: Paul Reesman
"""
import os
from collections import defaultdict


def accumulator(tweets):
    
    tweet_count = defaultdict(int)
    
    #Loop through each tweet in tweets
    for tweet in tweets:
        #Loop through each word in the tweet
        for word in tweet.split():
            tweet_count[word] += 1


def main():
    
    #Open file containing tweets as tweet_file
    with open("../tweet_input/tweets.txt") as tweet_file:
        #Read in content of tweet_file to a list variable, tweets
        tweets = tweet_file.readlines()
        #Send tweets as argument to accumulator function
        accumulator(tweets)
        
            


if __name__ == "__main__":
    main()