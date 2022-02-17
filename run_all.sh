#for i in ${!pref_type[@]}; do
#    for FILE in dpc3_traces/*; do    
#        ./run_champsim.sh ${pref_type[$i]} 50 50 $FILE &
#    done
#    wait
#done

cores=16

for FILE_B in bin/*; do
    for FILE_T in trace/*; do
        echo $FILE_B\_$FILE_T
        $FILE_B --warmup_instructions 10000000 --simulation_instructions 100000000 $FILE_T > results/${FILE_B##*/}\_${FILE_T##*/} &
        background=( $(jobs -p | wc -l) )
        if [ $background -ge $cores ]
        then
            echo waiting...
            wait -n
        fi
    done
done
