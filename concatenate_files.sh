# Concatenates all CSV files for included symbols
for s in `seq 1 30` #range of lines from text file
do
	symbol=`sed "${s}q;d" dow_jones_stocks.txt`
    cat ${symbol}*".csv" > "all${symbol}.csv"
done
