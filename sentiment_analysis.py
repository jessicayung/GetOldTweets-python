from textblob import TextBlob
import numpy as np
import csv

tweet_column = 4 # zero-indexed
tweets = []
tweets_sentiment_scores = []
file_path = "aapl250.csv"
# Get tweets (fifth column of CSV)
with open(file_path, 'rb') as f:
        mycsv = csv.reader(f, delimiter=";")
        for row in mycsv:
            tweet = row[tweet_column]
            # We don't want the header
            if tweet != 'text':
                tweet = ''.join([i for i in tweet if ord(i) < 128])
                tweets.append(tweet)
                tweets_sentiment_scores.append(TextBlob(tweet).sentiment.polarity)


print "Number of tweets: ", len(tweets), "Number of sentiment scores: ", len(tweets_sentiment_scores)
print "Mean: ", np.mean(tweets_sentiment_scores)
print "Std: ", np.std(tweets_sentiment_scores)
print "Sample tweet: ", tweets[:10:2]
print "Sample tweet sentiment score: ", tweets_sentiment_scores[:10:2]
