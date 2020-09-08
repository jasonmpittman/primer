#!/usr/bin/env python3

from scapy.all import *
from scapy.utils import rdpcap


def get_dst_mac(dst_ip):
    """

    Args:

    Returns:

    """
    ans,unans = arping(dst_ip, verbose=0)
    for s,r in ans:
        #print("{} {}".format(r[Ether].src,s[ARP].pdst))
        return r[Ether].src

def read_pcap(pcap, dst_ip):
    """

    Args:

    Returns:

    """
    new_src_mac = Ether().src
    new_src_ip = get_if_addr(conf.iface)
    new_dst_ip = dst_ip
    new_dst_mac = get_dst_mac(new_dst_ip)

    packets = rdpcap(pcap)

    for packet in packets:
        packet[Ether].src = new_src_mac
        packet[Ether].dst = new_dst_mac
        packet[IP].src = new_src_ip
        packet[IP].dst = new_dst_ip
        del packet[IP].chksum 
        sendp(packet)

read_pcap('../pcap/simplePing.pcap', '172.18.0.104')