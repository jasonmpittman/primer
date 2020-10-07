import pcap
import os 

class pcaps():
  def __init__(self, logging):
    self.pcaps([])
    self.createPcaps()
    self.logging = logging

  @property
  def pcaps(self):
    return self.pcaps

  def pcaps(self, pcaps):
    self.pcaps = pcaps

  def getPcaps():
    return self.pcaps

  def createPcaps(self):
    #read in the pcaps
    pcapFiles = os.listdir(path='../pcap/')
    print("pcap files: ")
    print(pcapFiles)
    for name in pcapFiles:
      #create a new object with the name of the pcap file name
      newPcap = pcap.pcap(name)
      #read the config file until we find the matching pcap name
      self.readConfig(name, newPcap)
      #append the fully detailed pcap file to the collection
      self.pcaps.append(newPcap)


  def readConfig(self, name, pcap):
      file = open("../config/pcapInfo.csv", "r")
      #pcapName,service,source,destination
      for line in file:
          pcapInfo = line.split(',')
          if(pcap._name == name):
            pcap.setName(pcapInfo[0])
            pcap._service(pcapInfo[1])
            pcap._sourceIp(pcapInfo[2])
            pcap._destinationIp(pcapInfo[3])
