
class PrimerEngine():
  def __init__(self, newNetworking):
    self._networking = newNetworking
    self._packets = [None]

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

  def generate_packets(self):
    return


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
        logging.info("=========================================================================================\n RUNNING " + str(selectedPcaps[pcapCount]) + " \n")
        generate_packets()
        # pcapDict = testTools.getPcapIps()
        # PREVIOUS_SOURCE_IP = testTools.getPreviousSource(pcap, pcapDict)
        # PREVIOUS_DESTINATION_IP = testTools.getPreviousDestination(pcap, pcapDict)
        # selected[service].append(pcap)
        # command = "tcpreplay-edit -i " + interface + " -S "  + PREVIOUS_SOURCE_IP + ":" + CURRENT_SOURCE_IP + " -D " + PREVIOUS_DESTINATION_IP + ":" + honeypotIP + " ../pcap/" + pcap
        # logging.info(command)
        # try:
        #   print("running command")
        #   output = subprocess.check_output(['bash', '-c', command])
        #   #logging.error(output.error())
        #   logging.info(output)
        # except Exception as e:
        #   print("caught error")
        #   successFlag = False
        #   logging.error(str(e))
        #   logging.error(str(RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))))
        # finally:
        #   logging.info("Next Pcap")
        #   #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        logging.info("=========================================================================================\n")
      pcapCount += 1
  return successFlag
