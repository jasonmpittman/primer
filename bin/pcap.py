
class pcap():
  _name()
  _sourceIp()
  _destinationIp()
  _service()

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