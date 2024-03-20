import pyshark
import os

CSV_PATH = ""

# Path for the pcap files
PCAP_PATH = ""

# Filter for suspicious packets
sus_filter = ""

# Filter for anomalous packets
ano_filter = ""

# Column names for the csv
COLUMNS = ""

# Open file for the labelled data
labeled = open(CSV_PATH, 'w', newline='')

# Write the columns in the csv file
labeled.write(COLUMNS)

# Use the small files to parse through
files = os.listdir(PCAP_PATH)
# for each small file
for file in files:
        # Get the pcap packets
        packets = pyshark.FileCapture(file, keep_packets=False)
        # run tshark filtering commands to get the suspicious packets
        sus_packets = pyshark.FileCapture(file, display_filter=sus_filter)
        # run thsark filtering commands to get the anomalous packets
        ano_packets = pyshark.FileCapture(file, display_filter=ano_filter)

        # for each row in the file
        for packet in packets:
            print(packet.time)
            # check if row is suspicious or anomalous, and add the label

        # add the final csv file into the big csv