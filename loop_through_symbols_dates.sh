## How to use this script
## 1. Looping through years
# For 2016: set year to 2016 and dates seq (line 17) to `seq 245 366`
# This takes dates from line 245-366 of dates2016.txt, i.e. from 1 Sept to 31 Dec 2016.
# For 2017: set year to 2017 and seq in line 17 to `seq 1 273` (1 Jan to 30 Sept 2017).

## 2. Looping through symbols
# This script loops through lines in the text file dow_jones_stocks.txt. You can change this in line 15.
# To get tweets for only a few symbols, change seq in line 15 or use loop_through_dates.sh.

year=2016
file="dates${year}.txt"
for s in `seq 1 30` #TODO: set lines to loop through in text file here
do
	symbol=`sed "${s}q;d" dow_jones_stocks.txt`
    echo $symbol
	for i in `seq 366 366` #TODO: set range of dates to loop through in chosen year here
	do
        j=$(($i+1))
	    start_date=`sed "${i}q;d" $file`
        if [[ "$i" -eq 366 ]]; then
            echo "i = 366"
            end_date="2017-01-01"
        else
		    end_date=`sed "${j}q;d" $file`
        fi
        echo $start_date, $end_date, $i
        filename="$symbol${year}_$i.csv"
		python Exporter.py --querysearch $symbol --since $start_date --until $end_date --output $filename
	done
done


