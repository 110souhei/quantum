ARRAY=(1 2 3 4 5 6 7 8 9 10)

for num in ${ARRAY[@]}; do
    /usr/bin/python ./random_norm1_8.py > ../in/8/$num.in
    echo $num"回目のループです"
done
