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
