
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

  def setName(self, value):
    self._name = value

  @property
  def sourceIp(self):
    return self._sourceIp

  def setSourceIp(self, value):
    self._sourceIp = value

  @property
  def destinationIp(self):
    return self._destinationIp

  def setDestinationIp(self, value):
    self._destinationIp = value

  @property
  def service(self):
    return self._service

  def setService(self, value):
    self._service = value
