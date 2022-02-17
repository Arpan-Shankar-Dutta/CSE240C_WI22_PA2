count=0
batch_size=16

for FILE in *; do
    #xz -d $FILE &
    let "count++"
    if [ $count -ge $batch_size ]
    then
        count=0
        echo launched $batch_size jobs, sleeping...
        wait
    fi
done


# hawkeye

signature number bits
occupancy vectore size

# ship++

rrcv value
