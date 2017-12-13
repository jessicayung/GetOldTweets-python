from textblob import TextBlob
import numpy as np
import csv
import math

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

num_scores = len(tweets_sentiment_scores)
print "Number of tweets: ", len(tweets), "Number of sentiment scores: ", num_scores
sum_scores = sum(tweets_sentiment_scores)
mean_score = sum_scores/num_scores
sse = sum([(score_i-mean_score)**2 for score_i in tweets_sentiment_scores])
# print "SSE: ", sse
print "Mean: ", mean_score
std_scores = math.sqrt(1.0/(num_scores-1) * sse)
print "Std: ", std_scores

print "Sample tweet: ", tweets[:10:2]
print "Sample tweet sentiment score: ", tweets_sentiment_scores[:10:2]
