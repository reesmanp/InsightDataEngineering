# InsightDataEngineering
Insight Data Engineering Coding Challenge

Python
------

I implemented both features, median_unique and words_tweeted, in python. 
Running with python 2.7.9, I made full use of the threading module and dictionaries.
Specifically I made full use of a subclass of dictionary, called defaultdict.
I made sure to create a defaultdict with the type being of type int, allowing me to easily increment values.

words_tweeted.py opens tweets.txt and reads in the tweets. 
The program then iterates over each word in each tweet and adds the word to a dictionary and inrements the value to the words' key.
The words' key happens to be the word itself. The program then writes to ft1.txt.
The output is:
unique_word    amount

median_unique.py opens tweets.txt and reads in the tweets.
The program iterates over each tweet and creates a thread, sending the thread to a new function with the tweet as the argument.
The thread then finds each unique word just like words_tweeted.py.
After each word in the tweet has been identified, the thread finds how many unique words there were.
The thread then attains a lock and updates a global variable which adds the amount of unique words in that tweet to a list.
The thread returns
The list is then sorted and a function finds the median value. The value is then written to ft2.txt