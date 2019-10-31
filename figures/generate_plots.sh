for i in $(ls *.py); do
        echo $i
        python3 $i
done
