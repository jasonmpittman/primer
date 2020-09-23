
class pcap():
  _name()
  _sourceIp()
  _destinationIp()
  _service()

  @property
  name(self):
    return self._name
  
  name.setter(self, value):
    self._name = value

  @property
  sourceIp(self):
    return self._sourceIp
  
  sourceIp.setter(self, value):
    self._sourceIp = value

  @property
  destinationIp(self):
    return self._destinationIp
  
  destinationIp.setter(self, value):
    self._destinationIp = value