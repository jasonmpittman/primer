
class pcaps():
  _pcaps[]

  @property
  def pcaps(self):
    return self._pcaps
  
  def __pcaps.setter(self, pcap):
    self.__pcaps = pcap

  def getPcaps():
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps