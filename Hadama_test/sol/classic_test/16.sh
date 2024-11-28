ARRAY=(1 2 3 4 5 6 7 8 9 10)

for num in ${ARRAY[@]}; do
    /usr/bin/python ../classic.py < ../../in/16/$num.in > ../../out/16/classic/$num.out
    echo $num"回目のループです"
done
