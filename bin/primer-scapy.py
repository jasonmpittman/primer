#!/usr/bin/env python3

from scapy.all import *
from scapy.utils import rdpcap


def get_dst_mac(src_ip, dst_ip):
    #packet = Ether(dst='ff:ff:ff:ff:ff')/ARP(pdst=dst_ip)
    #answered,unanswered = sendp(packet)
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=dst_ip),timeout=2)
    print(ans)
    #return answered[0][1][ARP].hwsrc

new_src_mac = Ether().src
new_src_ip = get_if_addr(conf.iface)

new_dst_ip = "10.0.1.1"
new_dst_mac = get_dst_mac(new_src_ip, new_dst_ip)

#packets = rdpcap(" pcap.")

#for packet in packets:
#    packet[Ether].src = new_src_mac
#    packet[Ether].dst = new_dst_mac

#    packet[IP].src = new_src_ip
#    packet[IP].dst = new_dst_ip

#    sendp(packet)

print(new_src_mac)
print(new_src_ip)

print(new_dst_ip)
print(new_dst_mac)