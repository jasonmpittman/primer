import socket
import netifaces as ni


PREVIOUS_SOURCE_IP = "172.16.0.137"
PREVIOUS_DESTINATION_IP = "172.16.0.201"

def getInterfaceList():
    #getting possible net interfaces for the current ip
    interfaces_list = ni.interfaces()
    return interfaces_list

def getCurrentIP(interface):
    return ni.ifaddresses('eth1')[ni.AF_INET][0]['addr']

#replace with dynamic pcap ip retrieval
def getPreviousDestination(pcap):
    return PREVIOUS_DESTINATION_IP

def getPreviousSource(pcap):
    return PREVIOUS_SOURCE_IP
