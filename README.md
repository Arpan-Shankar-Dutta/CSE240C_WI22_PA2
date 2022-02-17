<p align="center">
  <h1 align="center"> CSE240C_WI22_PA2 </h1>
</p>

# Clone this repository
```
git clone https://github.com/Arpan-Shankar-Dutta/CSE240C_WI22_PA2.git
```

# Important directories

1. ```trace``` contains all the championship traces.
2. ```results``` contains all results of all the simulations.
3. ```json``` files are in the parent directory. These are the files that are read but ```config.sh``` to make necessary changes to course code.
5. All simulations were run on all 83 single core traces. All simulation used 10M + 100M instructions for warmup and 50M actual instructions on which the IPC and MPKI was calculated.

# Instructions for running and reproducing the data

1. Run ```./build_all.sh```. This compiles all the source files.
2. Run ```./run_all.sh```. This will run all simulations in parallel.
3. Run ```python3 parse.py```. This is python script for collecting all data and geometric means for all the simulations. It provides separate IPC geo-means of all the prefetcher configurations for client, server and spec workloads separately and a cumulative geo-mean for all workloads taken together. The file ```IPC.csv``` is the output of the script. It also outputs pngs that can be viewed.
