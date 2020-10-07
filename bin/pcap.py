
class pcap():
  def __init__(self, newName):
    self._name(newName)
    #self._sourceIp()
    #self._destinationIp()
    #self._service()
    #self.readConfig()

  @property
  def _name(self):
    return self._name

  def _name(self, value):
    self._name = value

  def setName(self, value):
    self._name = value

  @property
  def _sourceIp(self):
    return self._sourceIp

  def _sourceIp(self, value):
    self._sourceIp = value

  def setSourceIp(self,value):
    self._sourceIp = value

  @property
  def _destinationIp(self):
    return self._destinationIp

  def _destinationIp(self, value):
    self._destinationIp = value

  @property
  def _service(self):
    return self._service

  def _service(self, value):
    self._service = value
