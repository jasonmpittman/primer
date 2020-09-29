
class PrimerEngine():

  _networking()
  _packets[]

  @property
  def packets(self):
    return self._Packets

  def _packets.setter(self, value):
    self._packets = value

  @property
  def networking(self):
    return self._networking

  def _networking.setter(self, value):
    self._networking = value

  def generate_packets():
    return

  def handle_run(self):
    #Mapping to service -> pcap
    selected =  {
      "service": ["example.pcap"]
    }
    selected.clear()

    servicePcapMap = primerFacade.getServicePcapMap()
    #retrieve info from fields
    _networking.honeypotIP = self.honeyPotEntry.get()
    interface = self.interfaceMenu.get()
    #get the current source IP from the testTools file
    CURRENT_SOURCE_IP = testTools.getCurrentIP(interface)
    #logging.info('running following services/pcaps:' + str(selected))

    #run the selected Pcaps
    success = self.runPcaps(servicePcapMap, interface, selected, self.selectedPcaps)

    #After running --> have a popup telling if it was successful or not
    if success:
      tk.messagebox.showinfo("Primer", "Command Ran Successfully")
    else:
      tk.messagebox.showinfo("Primer", "Pcaps ran with errors - see log file for details.\nLog located at: " + self.logFile)

  def runPcaps(d, interface, selected, selectedPcaps):
  successFlag = True
  #get the current source IP from the testTools file
  CURRENT_SOURCE_IP = testTools.getCurrentIP(interface)
  pcapCount = 0
  for service in d:
    selected[service] = []
    for pcap in d[service]:
      #selected Pcaps is the entire lsit of pcaps
      #.get() == 1 checks if the pcap is selected
      if(selectedPcaps[pcapCount].get() == 1):
        logging.info("=========================================================================================\n RUNNING " + str(selectedPcaps[pcapCount]) + " \n")
        pcapDict = testTools.getPcapIps()
        PREVIOUS_SOURCE_IP = testTools.getPreviousSource(pcap, pcapDict)
        PREVIOUS_DESTINATION_IP = testTools.getPreviousDestination(pcap, pcapDict)
        selected[service].append(pcap)
        command = "tcpreplay-edit -i " + interface + " -S "  + PREVIOUS_SOURCE_IP + ":" + CURRENT_SOURCE_IP + " -D " + PREVIOUS_DESTINATION_IP + ":" + honeypotIP + " ../pcap/" + pcap
        logging.info(command)
        try:
          print("running command")
          output = subprocess.check_output(['bash', '-c', command])
          #logging.error(output.error())
          logging.info(output)
        except Exception as e:
          print("caught error")
          successFlag = False
          logging.error(str(e))
          logging.error(str(RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))))
        finally:
          logging.info("Next Pcap")
          #raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        logging.info("=========================================================================================\n")
      pcapCount += 1
  return successFlag
