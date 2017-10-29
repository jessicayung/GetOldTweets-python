year=2016
file="dates${year}.txt"
for symbol in "\$AAPL"
do
	for i in `seq 1 3`
	do
        #echo $i
        j=$(($i+1))
        #echo $j
	    start_date=`sed "${i}q;d" $file`
        echo "start_date added"
		end_date=`sed "${j}q;d" $file`
        filename="$symbol${year}_$i.csv"
		python Exporter.py --querysearch $symbol --since $start_date --until $end_date --output $filename
	done
done


