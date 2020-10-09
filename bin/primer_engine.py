from scapy.all import *
from scapy.utils import rdpcap
import logging 

class PrimerEngine():
  def __init__(self, newNetworking, logging):
    self._networking = newNetworking
    self._packets = [None]
    self.logging = logging

  @property
  def packets(self):
    return self._Packets

  def _setPackets(self, value):
    self._packets = value

  @property
  def networking(self):
    return self._networking

  def _setNetworking(self, value):
    self._networking = value

  def readPcap(self, pcap, dst_ip):
    """

    Args:

    Returns:

    """
    self._networking.setHost_mac(Ether().src)
    self._networking.setTarget_ip(dst_ip) 
    self._networking.setDestination_mac(get_dst_mac(new_dst_ip))

    self._Packets = rdpcap(pcap)

  def generate_packets():
    for packet in self._Packets:
        packet[Ether].src = self._networking.host_mac()
        packet[Ether].dst = self._networking.target_mac()
        packet[IP].src = self._networking.host_ip()
        packet[IP].dst = self._networking.target_ip()
        del packet[IP].chksum 
        sendp(packet)





  def get_dst_mac(dst_ip):
    """

    Args:

    Returns:

    """
    ans,unans = arping(dst_ip, verbose=0)
    for s,r in ans:
        #print("{} {}".format(r[Ether].src,s[ARP].pdst))
        return r[Ether].src



  def run(self, pcap):
    self.readPcap(pcap, self._networking.target_ip())
    self.generate_packets()
    

  def runPcaps(self, servicePcapMap, selectedPcaps):
    successFlag = True
    #get the current source IP from the testTools file
    CURRENT_SOURCE_IP = self.networking.sourceIp()
    pcapCount = 0
    for service in servicePcapMap:
      selected[service] = []
      for pcap in servicePcapMap[service]:
        #selected Pcaps is the entire lsit of pcaps
        #.get() == 1 checks if the pcap is selected
        if(selectedPcaps[pcapCount].get() == 1):
          self.logging.info("==========================================================\n RUNNING " + str(selectedPcaps[pcapCount]) + " \n")
          readPcap(pcap, self._networking.target_ip())
          generate_packets()
          # pcapDict = testTools.getPcapIps()
          # PREVIOUS_SOURCE_IP = testTools.getPreviousSource(pcap, pcapDict)
          # PREVIOUS_DESTINATION_IP = testTools.getPreviousDestination(pcap, pcapDict)
          # selected[service].append(pcap)
          # command = "tcpreplay-edit -i " + interface + " -S "  + PREVIOUS_SOURCE_IP + ":" + CURRENT_SOURCE_IP + " -D " + PREVIOUS_DESTINATION_IP + ":" + honeypotIP + " ../pcap/" + pcap
          # self.logging.info(command)
          try:
            print("running command")
            output = subprocess.check_output(['bash', '-c', command])
            #self.logging.error(output.error())
          #   self.logging.info(output)
          except Exception as e:
             print("caught error")
             successFlag = False
             self.logging.error(str(e))
             self.logging.error(str(RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))))
          finally:
             self.logging.info("Next Pcap")
             #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
          self.logging.info("======================================================================\n")
        pcapCount += 1
    return successFlag
