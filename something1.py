from Kitsune import Kitsune
import numpy as np
import time
import pickle
import psutil
# from memory_profiler import profile

f_prof = open("memory_profile.log", 'w+')

@profile
def generate_RMSES(stream = f_prof):
    # Make a function with the following: process.cpu_percent, memory_info, consider memory_percent maybe?,  
    # The file where we store the memory usage logs
    fp=open('memorytest.log','w+')

    # Get the process of the current program
    process = psutil.Process()

    # Name of the sample capture zip file
    # capture = ""
    # Name of the pcap file
    capture_pcap = "D:\\Teasis_data\\MAWI\\final_mawi1.pcap.tsv"
    # Number of packets to process
    packet_limit = np.Inf
    # How often to display the number of processed packets
    display_freq = 10000

    # KitNET params
    # Max autoencoder size in the ensemble layer
    maxAE_size = 10
    # Number of instances for learning the feature mapping
    FMinstances = 53320
    # Number of instances for training the anomaly detector
    ADinstances = 1053323


    # Call cpu_percent to measure how much CPU is used to build Kitsune
    process.cpu_percent()
    # Measure RAM usage before starting Kitsune
    ram_before = process.memory_info().vms

    # Build Kitsune
    K = Kitsune(capture_pcap, packet_limit, maxAE_size, FMinstances, ADinstances)

    # Measure RAM usage after building Kitsune
    ram_after = process.memory_info().vms

    # Measure the CPU percentage while building Kitsune
    fp.write("CPU percentage used while building Kitsune: " + str(process.cpu_percent()) + "\n")
    # Measure RAM after building Kitsune
    fp.write("RAM used while building Kitsune: " + str(ram_after-ram_before) + "\n")

    print("Running Kitsune:")
    RMSEs = []
    i = 0

    # Call cpu_percent to measure how much CPU is used to process packets
    process.cpu_percent() 
    # Measure RAM usage before processing packets
    ram_before = process.memory_info().vms

    start = time.time()
    # Processing the packets
    while True:
        i +=1
        if i % display_freq == 0:
            print(i)
            print("Current time: " + str(start - time.time()))

        # Process the next packet
        rmse = K.proc_next_packet()

        # Stop the loop if there are no more packets
        if rmse == -1:
            break
        # Otherwise append the rmse
        RMSEs.append(rmse)
    stop = time.time()

    # Measure RAM usage after processing packets
    ram_after = process.memory_info().vms

    # Measure the CPU percentage while processing packets
    fp.write("CPU percentage used while processing packets: " + str(process.cpu_percent()) + "\n")
    # Measure RAM after processing packets
    fp.write("RAM used while processing packets: " + str(ram_after-ram_before) + "\n")

    # Save the results in a pickle file
    pickle.dump(RMSEs, open("test_results_test.p", "wb"))
    # The end :)
    print("All packets have been processed. Time elapsed: " + str(stop - start))

if __name__ == "__main__":
    generate_RMSES()