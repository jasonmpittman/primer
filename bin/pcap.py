
class pcap():
  def __init__(self, newName):
    self._name(newName)
    self._sourceIp()
    self._destinationIp()
    self._service()
    self.readConfig()

  @property
  def name(self):
    return self._name

  def name.setter(self, value):
    self._name = value

  @property
  def sourceIp(self):
    return self._sourceIp

  def sourceIp.setter(self, value):
    self._sourceIp = value

  @property
  def destinationIp(self):
    return self._destinationIp

  def destinationIp.setter(self, value):
    self._destinationIp = value

  def readConfig(self):
      open("../config/pcapInfo.csv")
