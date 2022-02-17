for FILE in *.json; do
    cp -rf hawkeye.cc replacement/hawkeye/
    cp -rf shipPlusPlus.cc replacement/shipPlusPlus/
    ./config.sh $FILE
    make
done

#for i in ${!pref_type[@]}; do
#    ./build_champsim.sh hashed_perceptron ${pref_type[$i]} next_line spp_dev no lru 1
#done
