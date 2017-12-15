from textblob import TextBlob
import numpy as np
import csv
import sys

# TODO: Set parameters
stock = sys.argv[1][1:]
has_folder = False

file_prefix = "$" + stock.upper()
tweet_column = 4 # zero-indexed

# Construct list of dates
dates = []
# add 2016 days
for i in range(245,366+1):
    dates.append("2016_" + str(i))
# add 2017 days
for i in range(1,273+1):
    dates.append("2017_" + str(i))

# Construct list of actual dates
list_of_actual_dates = []
with open("dates2016.txt") as f:
    for i, line in enumerate(f):
        if i >= 245 - 1:
            list_of_actual_dates.append(line)
with open("dates2017.txt") as f:
    for i, line in enumerate(f):
        if i < 273:
            list_of_actual_dates.append(line)

# initialise stock CSV
with open(stock + "_scores.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'CSV no.', 'Stock', 'Mean', 'Stdev', 'No. tweets'])


# Compute scores and write to CSVs
for j, day in enumerate(dates):
    print "Processing day: ", day
    filename = file_prefix + day + ".csv"
    if has_folder:
        file_path = "data/" + str(stock) + "/" + filename
    else:
        file_path = "data/" + filename

    tweets = []
    tweets_sentiment_scores = []
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

    # Add mean sentiment score to CSV
    with open(stock + "_scores.csv", "a") as f:
        writer = csv.writer(f)
        mean = np.mean(tweets_sentiment_scores)
        stdev = np.std(tweets_sentiment_scores, ddof=1)
        num_tweets = len(tweets_sentiment_scores)
        writer.writerow([list_of_actual_dates[j], day, stock, mean, stdev, num_tweets]) # day = file date code

    with open("scores/" + filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow("Tweet sentiment score")
        for score in tweets_sentiment_scores:
            writer.writerow(str(score))

"""
print "Number of tweets: ", len(tweets), "Number of sentiment scores: ", len(tweets_sentiment_scores)
print "Mean: ", np.mean(tweets_sentiment_scores)
print "Std: ", np.std(tweets_sentiment_scores)
print "Sample tweet: ", tweets[:10:2]
print "Sample tweet sentiment score: ", tweets_sentiment_scores[:10:2]
"""
