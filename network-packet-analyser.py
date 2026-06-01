from scapy.all import sniff
from scapy.layers.inet import IP

def protocol_name(protocol):

    if protocol == 6:
        return "TCP"
    elif protocol == 17:
        return "UDP"
    elif protocol == 1:
        return "ICMP"
    else:
        return "Other"

def packet_callback(packet):

    if packet.haslayer(IP):

        source = packet[IP].src
        destination = packet[IP].dst
        protocol = protocol_name(packet[IP].proto)

        print("\n----------------------")
        print("Source IP      :", source)
        print("Destination IP :", destination)
        print("Protocol       :", protocol)

print("Starting Packet Capture...\n")

sniff(prn=packet_callback, store=False)