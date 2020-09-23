class Networking():
  _HostMac
  _HostIp
  _TargetMac
  _TargetIp
  _Interfaces


  @property
  def host_mac(self):
    return self._HostMac

  def host_mac.setter(self, value):
    self._HostMac = value

  @property
  def host_ip(self):
    return self._HostIp

  def host_ip.setter(self, value):
    self._HostIp = value

  @property
  def target_mac(self):
    return self._TargetMac

  def target_mac.setter(self, value):
    self._TargetMac = value

  @property
  def target_ip(self):
    return self._TargetIp

  def target_ip.setter(self, value):
    self._TargetIp = value

  @property
  def interfaces(self):
    return self.interfaces

  def interfaces.setter(self, value):
    self.interfaces = value