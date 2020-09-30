from getmac import get_mac_address as gma
import socket
import netifaces as ni

class Networking():
  def __init__(self):
    self._HostMac = gma()
    self._HostIp = None
    self._TargetMac = None
    self._TargetIp = None
    self._Interfaces = self.fetchInterfaces()


  @property
  def host_mac(self):
    return self._HostMac

  def setHost_mac(self, value):
    self._HostMac = value

  @property
  def host_ip(self):
    return self._HostIp

  def setHost_ip(self, value):
    self._HostIp = value

  @property
  def target_mac(self):
    return self._TargetMac

  def setTarget_mac(self, value):
    self._TargetMac = value

  @property
  def target_ip(self):
    return self._TargetIp

  def setTarget_ip(self, value):
    self._TargetIp = value

  @property
  def interfaces(self):
    return self.__Interfaces

  def setInterfaces(self, value):
    self.__Interfaces = value

  def setHostIpRuntime(self, interface_choice):
      self.__HostIp = ni.ifaddresses(interface_choice)[ni.AF_INET][0]['addr']

  def fetchInterfaces(self):
    interfaces_list = ni.interfaces()
    return interfaces_list
