from scapy.all import *

def generate_filter(filters):
    final_filter = ""

    # Go through each filter an add it to the final filter
    for filter in filters[:-1]:
        # Negate the filter (because we want packets that aren't anomalous or suspicious) and add it to the final filter
        final_filter += "not (" + filter + ") && "
    
    # Add the last filter
    final_filter += "not (" + filters[-1] + ")"

    return final_filter
            
# Set the pcap file path
PCAP_FILE = 'D:\\Teasis_data\\MAWI\\mawi_00001_20240124060002.pcap'
# The list of filters for anomalies
filter_list = [
    "(ip.dst == 203.188.123.191 && tcp.dstport == 10022) || (ip.dst == 203.188.123.191)",
    "ip.src == 202.4.51.123 && tcp.dstport == 443",
    "(ip.dst == 203.188.123.167 && tcp.dstport == 80) || (ip.dst == 203.188.123.167)",
    "ip.dst == 202.4.51.25 && tcp.srcport == 443",
    "(ip.dst == 150.162.249.131 && ip.src == 180.199.213.103) || (ip.dst == 150.162.249.131 && tcp.dstport == 80) || (ip.dst == 203.188.118.16 && ip.src == 180.199.213.103 && tcp.dstport == 80)",
    "((ip.src == 203.188.123.167) && (tcp.srcport == 80)) || (ip.src == 203.188.123.167)",
    "((ip.dst == 202.4.51.122) && (tcp.srcport == 443)) || ((ip.dst == 202.4.51.119) && (tcp.srcport == 443))",
    "((ip.dst == 202.4.51.120) && (tcp.srcport == 443))",
    "((ip.dst == 202.4.51.121) && (tcp.srcport == 443))",
    "((ip.src == 203.188.118.16) && (tcp.srcport == 80))",
    "((ip.src == 163.245.215.207) && (tcp.dstport == 443))",
    "(ip.dst == 150.162.249.131) && ((tcp.dstport == 443) || (tcp.dstport == 80))",
    "((ip.src == 203.188.123.167) && (tcp.srcport == 80)) || ((ip.src == 203.188.123.167))",
    "((ip.src == 150.162.249.131) && (tcp.srcport == 80)) || ((ip.src == 150.162.249.131) && (tcp.srcport == 443)) || ((ip.src == 203.188.123.167) && (tcp.srcport == 80))",
    "(ip.src == 157.140.162.184) && (ip.dst == 3.22.106.199) && (tcp.dstport == 443)",
    "((ip.dst == 203.188.125.160) && (tcp.dstport == 26190)) || (ip.dst == 203.188.125.160)",
    "(ip.dst == 131.62.216.24)",
    "(ip.src == 203.188.125.160) || ((ip.src == 203.188.125.160) && (tcp.srcport == 26190))",
    "(ip.src == 202.4.51.61) && (ip.dst == 18.69.105.227) && (tcp.dstport == 443)",
    "((ip.dst == 203.188.123.191) && (tcp.dstport == 10022)) || (ip.dst == 203.188.123.191)",
    "(ip.src == 131.62.216.24) && (((ip.dst == 94.125.246.135) && (tcp.srcport == 4500) && (tcp.dstport == 4980)) || ((ip.dst == 157.130.102.190) && (tcp.srcport ==60000) && (tcp.dstport == 443)) || ((ip.dst == 192.50.25.191) && (tcp.srcport == 587) && (tcp.dstport == 33083)) || ((ip.dst == 162.255.241.29) && (tcp.srcport == 587) && (tcp.dstport == 50688)))",
    "((ip.src == 203.188.123.191) && (tcp.srcport == 10022)) || (ip.src == 203.188.123.191)"
]

# Set the filter criteria
FILTER = generate_filter(filter_list)
print(FILTER)
