import pcap
class pcaps():
  def __init__(self):
    self._pcaps = [None]

  @property
  def pcaps(self):
    return self._pcaps

  def __pcaps.setter(self, pcap):
    self.__pcaps = pcap

  def getPcaps():
    return __pcaps

  def createPcaps():
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    for x in pcaps:
      #create a new object with the name of the pcap file x
      newPcap = pcap(x)
      self.readConfig(x, newPcap)

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
