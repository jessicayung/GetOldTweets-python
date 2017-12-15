## How to use this script
## 1. Looping through years
# For 2016: set year to 2016 and seq to `seq 245 366`
# This takes dates from line 245-366 of dates2016.txt, i.e. from 1 Sept to 31 Dec 2016.
# For 2017: set year to 2017 and seq to `seq 1 273` (1 Jan to 30 Sept 2017).

## 2. Looping through symbols
# To set a query term, edit for symbol in "YOUR_TERM_HERE" in line 11.
# Note: if you want to search for something with a $ in it, you need to put a backslash before it like so: "\$AAPL". This is because $ is a character to get the value of a variable in bash (this programming language).


year=2016
file="dates${year}.txt"
for symbol in "\$AAPL"
do
	for i in `seq 1 3`
	do
        j=$(($i+1))
	    start_date=`sed "${i}q;d" $file`
		end_date=`sed "${j}q;d" $file`
        filename="$symbol${year}_$i.csv"
		python Exporter.py --querysearch $symbol --since $start_date --until $end_date --output $filename
	done
done


