ARRAY=(1 2 3 4 5 6 7 8 9 10)

for num in ${ARRAY[@]}; do
    /usr/bin/python ../classic.py < ../../in/8/$num.in > ../../out/8/classic/$num.out
    echo $num"回目のループです"
done
