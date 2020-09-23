class Networking():
  _HostMac
  _HostIp
  _TargetMac
  _TargetIp
  _Interfaces


  @property
  host_mac(self):
    return self._HostMac

  host_mac.setter(self, value):
    self._HostMac = value

  @property
  host_ip(self):
    return self._HostIp

  host_ip.setter(self, value):
    self._HostIp = value

  @property
  target_mac(self):
    return self._TargetMac

  target_mac.setter(self, value):
    self._TargetMac = value

  @property
  target_ip(self):
    return self._TargetIp

  target_ip.setter(self, value):
    self._TargetIp = value

  @property
  interfaces(self):
    return self.interfaces

  interfaces.setter(self, value):
    self.interfaces = value