
for i in 10 100 1000 10000 100000 1000000 10000000 100000000
do
(time  python $1.py 1 2 $i) 2> datanon.dat
echo -n $i ' '
head -3 datanon.dat | tail -1 | cut -c8-12
done

rm datanon.dat
