from http import client
import numpy as np
import glob
import matplotlib.pyplot as plt

def g_mean(x):
    a = np.log(x)
    return np.exp(a.mean())

pref_type = ["lru",
             "ship_",
             "hawkeye_base",
             "shipPlusPlus_base",
             "hawkeye_maxRRPV_2",
             "hawkeye_maxRRPV_3",
             "hawkeye_base",
             "hawkeye_maxRRPV_11",
             "hawkeye_maxRRPV_15",
             "hawkeye_OPTGEN_VECTOR_SIZE_32",
             "hawkeye_OPTGEN_VECTOR_SIZE_64",
             "hawkeye_base",
             "hawkeye_OPTGEN_VECTOR_SIZE_256",
             "hawkeye_OPTGEN_VECTOR_SIZE_512",
             "hawkeye_SAMPLED_CACHE_SIZE_768",
             "hawkeye_SAMPLED_CACHE_SIZE_1400",
             "hawkeye_base",
             "hawkeye_SAMPLED_CACHE_SIZE_5600",
             "hawkeye_SAMPLED_CACHE_SIZE_11200",
             "shipPlusPlus_maxRRPV_2",
             "shipPlusPlus_base",
             "shipPlusPlus_maxRRPV_7",
             "shipPlusPlus_maxRRPV_11",
             "shipPlusPlus_maxRRPV_15",
             "shipPlusPlus_maxSHCTR_2",
             "shipPlusPlus_maxSHCTR_3",
             "shipPlusPlus_base",
             "shipPlusPlus_maxSHCTR_11",
             "shipPlusPlus_maxSHCTR_15",
             "shipPlusPlus_NUM_LEADER_SETS_16",
             "shipPlusPlus_NUM_LEADER_SETS_32",
             "shipPlusPlus_base",
             "shipPlusPlus_NUM_LEADER_SETS_128",
             "shipPlusPlus_NUM_LEADER_SETS_256"]

ipc_plt = []
mpki_plt = []
geomean_array = np.zeros((34,2,83))

out_file = open("./IPC.csv", "w")

out_file.write("Replacement,IPC,MPKI\n")

prf = 0

for pref in pref_type:
    path = "results/champsim_"+pref+"*"
    print(path)
    cm = 0
    temp_ipc = []
    temp_mpki = []
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for line in f.readlines():
                if "CPU 0 cumulative IPC:" in line:
                    value = line.rstrip('\n').split()
                    geomean_array[prf][0][cm] = float(value[4])
                    temp_ipc.append(float(value[4]))
                if "LLC TOTAL" in line:
                    value = line.rstrip('\n').split()
                    geomean_array[prf][1][cm] = float(value[7])/100000
                    temp_mpki.append(float(value[7])/100000)
        cm = cm + 1
    ipc_plt.append(temp_ipc)
    mpki_plt.append(temp_mpki)
    prf = prf + 1

for i in range(83):
    if geomean_array[10][0][i] == 0:
        geomean_array[10][0][i] = 0.1

for i in range(34):
    out_file.write(pref_type[i]+","+str(g_mean(geomean_array[i][0]))+","+str(np.mean(geomean_array[i][1]))+"\n")
    if i == 10:
        print(pref_type[i])
        print(geomean_array[i][0])

names = ["lru", "ship", "hawkeye", "shipPlusPlus"]
plt.boxplot(ipc_plt[0:4], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("baseline_ipc.png")
plt.clf() 

names = ["lru", "ship", "hawkeye", "shipPlusPlus"]
plt.boxplot(mpki_plt[0:4], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("baseline_mpki.png")
plt.clf() 

names = ["maxRRPV_2", "maxRRPV_3", "base", "maxRRPV_11", "maxRRPV_15"]
plt.boxplot(ipc_plt[4:9], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("hawkeye_maxRRPV_ipc.png")
plt.clf() 

names = ["maxRRPV_2", "maxRRPV_3", "base", "maxRRPV_11", "maxRRPV_15"]
plt.boxplot(mpki_plt[4:9], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("hawkeye_maxRRPV_mpki.png")
plt.clf() 

names = ["OPTGEN_32", "OPTGEN_64", "base", "OPTGEN_256", "OPTGEN_512"]
plt.boxplot(ipc_plt[9:14], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("hawkeye_OPTGEN_VECTOR_SIZE_ipc.png")
plt.clf() 

names = ["OPTGEN_32", "OPTGEN_64", "base", "OPTGEN_256", "OPTGEN_512"]
plt.boxplot(mpki_plt[9:14], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("hawkeye_OPTGEN_VECTOR_SIZE_mpki.png")
plt.clf() 

names = ["SIZE_768", "SIZE_1400", "base", "SIZE_5600", "SIZE_11200"]
plt.boxplot(ipc_plt[14:19], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("hawkeye_SAMPLED_CACHE_SIZE_ipc.png")
plt.clf() 

names = ["SIZE_768", "SIZE_1400", "base", "SIZE_5600", "SIZE_11200"]
plt.boxplot(mpki_plt[14:19], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("hawkeye_SAMPLED_CACHE_SIZE_mpki.png")
plt.clf() 

names = ["maxRRPV_2", "base", "maxRRPV_7", "maxRRPV_11", "maxRRPV_15"]
plt.boxplot(ipc_plt[19:24], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("shipPlusPlus_maxRRPV_ipc.png")
plt.clf() 

names = ["maxRRPV_2", "base", "maxRRPV_7", "maxRRPV_11", "maxRRPV_15"]
plt.boxplot(mpki_plt[19:24], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("shipPlusPlus_maxRRPV_mpki.png")
plt.clf() 

names = ["maxSHCTR_2", "maxSHCTR_3", "base", "maxSHCTR_11", "maxSHCTR_15"]
plt.boxplot(ipc_plt[24:29], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("shipPlusPlus_maxSHCTR_ipc.png")
plt.clf() 

names = ["maxSHCTR_2", "maxSHCTR_3", "base", "maxSHCTR_11", "maxSHCTR_15"]
plt.boxplot(mpki_plt[24:29], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("shipPlusPlus_maxSHCTR_mpki.png")
plt.clf() 

names = ["LEADER_16", "LEADER_32", "base", "LEADER_128", "LEADER_256"]
plt.boxplot(ipc_plt[29:34], labels=names)
plt.rc('font', size=10) 
plt.ylabel("IPC")
plt.savefig("shipPlusPlus_NUM_LEADER_SETS_ipc.png")
plt.clf() 

names = ["LEADER_16", "LEADER_32", "base", "LEADER_128", "LEADER_256"] 
plt.boxplot(mpki_plt[29:34], labels=names)
plt.rc('font', size=10) 
plt.ylabel("MPKI")
plt.savefig("shipPlusPlus_NUM_LEADER_SETS_mpki.png")
plt.clf()   
