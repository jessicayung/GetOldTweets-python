year=2016
file="dates${year}.txt"
echo $file
for symbol in "AAPL"
do
	for i in `seq 1 3`
	do
        #echo $i
        j=$(($i+1))
        echo $j
	    start_date= sed "${i}q;d" $file
		end_date= sed "${j}q;d" $file
        filename="$symbol${year}_$i.csv"
        echo $start_date $end_date $filename
		# python Exporter.py --querysearch $symbol --since $start_date --until $end_date --output $filename
	done
done


