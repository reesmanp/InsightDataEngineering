# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:19:03 2015

@author: Paul Reesman
"""
import os
import threading
from collections import defaultdict


class MedianUnique():
    
    def __init__(self):
        self.actual_median = []
        self.unique_words = []
        self.thread_list = []
        self.lock = threading.Lock()
    
    def find_median(self):
        #Sorts unique_words
        self.unique_words.sort()
        #Find the length of unique_words
        median_length = len(self.unique_words)
        #Loop through medianList; Find running median
        for index in range(median_length):
            #If there is an odd amount of elements up to the index
            if index % 2 == 0:
                #The median is the middle element
                self.actual_median.append(float(self.unique_words[index / 2]))
            #If there is an even amount of elements up to the index
            else:
                #Find the two middle indices of unique_words
                lower_bound = self.unique_words[index / 2]
                upper_bound = self.unique_words[(index / 2) + 1]
                #Calculates the median -- Finds average of middle indices
                #Uses float division notation
                self.actual_median.append((lower_bound + upper_bound) / 2.0)
    
    def __median(self, tweet):
        #Creates a local dictionary to store each unique word
        unique_dict = defaultdict(int)
        #Loops through each word in tweet
        for word in tweet.split():
            #Adds a dummy value to the key, word, which is unique
            unique_dict[word] += 1
        #Get a list of all the keys from unique_dict
        words = unique_dict.keys()
        #Find the length of words
        length = len(words)
        #Have this thread acquire the lock
        with self.lock:
            #Append the amount of unique words to unique_words
            self.unique_words.append(length)
    
    def median(self, tweets):
        #Loop through each tweet in tweets
        for tweet in tweets:
            #Creates a thread for each tweet
            thread = threading.Thread(target=self.__median, args=(tweet,))
            #Appends thread to thread_list
            self.thread_list.append(thread)
            #Starts the thread
            thread.start()
        
        for thread in self.thread_list:
            #Wait for all threads to terminate
            thread.join()
        #Calls find_median function to find the median unique word amount
        self.find_median()
    
    def main(self):
        #Open file containing tweets as tweet_file
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                + "/tweet_input/tweets.txt") as tweet_file:
            #Read in content of tweet_file to a list variable, tweets
            tweets = tweet_file.readlines()
            #Send tweets as argument to accumulator function
            self.median(tweets)
        
        #Open the file to write to
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                + "/tweet_output/ft2.txt", 'w') as write_file:
            #For each running median, write to file
            for element in self.actual_median:
                write_file.write("%.1f\n" % element)


if __name__ == "__main__":
    median_unique = MedianUnique()
    median_unique.main()