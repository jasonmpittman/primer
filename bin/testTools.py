import socket
import netifaces as ni


PREVIOUS_SOURCE_IP = "172.16.0.137"
PREVIOUS_DESTINATION_IP = "172.16.0.201"

def getInterfaceList():
  #getting possible net interfaces for the current ip
  interfaces_list = ni.interfaces()
  return interfaces_list

def getCurrentIP(interface):
  return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']

def getPcapIps():
   #Mapping to service -> pcap
  d =  {
  "x.pcap": ["1.1.1.1.1", "10.10.10.10.10"]
  }
  d.clear()
  file = open("../config/pcapIp.csv", "r")
  mappings = file.read().split("\n")
  #Adding the dictionary Key (PCap) to Values (Array of Src/Dest)
  for y in mappings:
    x = y.split(",")
    d.update( {x[0] : x[1::]} )

  return d

def getPreviousSource(pcap, d):
  return d[pcap][0]

def getPreviousDestination(pcap, d):
  return d[pcap][1]