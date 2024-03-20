import os

# Generate the mergecap command
def generate_command(directory, merge_path, output):
    command = merge_path + " -F pcap -w " + output + " "

    # Get a list of all the files in the directory
    files = os.listdir(directory)

    # Add the files to the command
    for file in files:
        command += file + " "
        
    print(command)

# Directory with pcap files to be merged
FILE_DIR = "D:\\Teasis_data\\MAWI\\small"

# Path of the output file
OUTPUT_PATH = "D:\\Teasis_data\\MAWI\\final_mawi.pcap"

# Path of mergecap.exe
MERGE_PATH = "\"C:\\Program Files\\Wireshark\\mergecap.exe\""

generate_command(FILE_DIR, MERGE_PATH, OUTPUT_PATH)