ARRAY=("1" "2" "3" "4" "5" "6" "7" "8" "9" "10")


for n in "4" "8"
     do
     echo $n"回目ー"
    for num in ${ARRAY[@]}; do
        python3 ../main100.py < ../../in/$n/$num.in > ../../out/$n/quantum/shot100/$num.out
        echo $num"回目のループです"
    done

    for num in ${ARRAY[@]}; do
        python3 ../main1e3.py < ../../in/$n/$num.in > ../../out/$n/quantum/shot1000/$num.out
        echo $num"回目のループです"
    done


    for num in ${ARRAY[@]}; do
        python3 ../main1e4.py < ../../in/$n/$num.in > ../../out/$n/quantum/shot10000/$num.out
        echo $num"回目のループです"
    done
done
