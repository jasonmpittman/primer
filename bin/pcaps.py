import pcap
class pcaps():
  __pcaps()
  
  def __init__(self):
    self._pcaps = [None]
    self.createPcaps()

  @property
  def pcaps(self):
    return self._pcaps

  def __pcaps.setter(self, pcaps):
    self.__pcaps = pcaps

  def getPcaps():
    return self.__pcaps

  def createPcaps():
    #read in the pcaps
    pcapFiles = os.listdir(path='pcap/')
    for name in pcapFiles:
      #create a new object with the name of the pcap file name
      newPcap = pcap(name)
      #read the config file until we find the matching pcap name
      self.readConfig(name, newPcap)
      #append the fully detailed pcap file to the collection
      self.__pcaps.append(newPcap)


  def readConfig(self, name, pcap):
      file = open("../config/pcapInfo.csv", "r")
      #pcapName,service,source,destination
      for line in file:
          pcapInfo = line.split(',')
          if(pcap.name == name):
            pcap.name.setter(pcapInfo[0])
            pcap.service.setter(pcapInfo[1])
            pcap.sourceIp.setter(pcapInfo[2])
            pcap.destinationIp.setter(pcapInfo[3])
