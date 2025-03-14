from scapy.all import *

suspicious_ip = "192.168.199.35"

def capture_packets(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if ip_src == suspicious_ip or ip_dst == suspicious_ip:
            print(f"Suspicious packet: {ip_src} -> {ip_dst}")
        else:
            print(f"Packet: {ip_src} -> {ip_dst}")

sniff(prn=capture_packets, filter="ip", store=0)
