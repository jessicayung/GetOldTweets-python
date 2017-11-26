
for s in `seq 1 1` #TODO: set lines to loop through in text file here
do
	symbol=`sed "${s}q;d" dow_jones_stocks.txt`
	dirname=$symbol
	mv \$$symbol* $dirname 
done
