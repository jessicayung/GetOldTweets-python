## Looping through symbols
# This script loops through lines in the text file dow_jones_stocks.txt.
# To only loop through a few symbols, change seq in line 15.

for s in `seq 1 30` #TODO: set lines to loop through in text file here
do
	symbol=`sed "${s}q;d" dow_jones_stocks.txt`
    echo $symbol
    python get_sentiment_scores.py $symbol
done
