# import honeypot
import logging
import test_tools
import subprocess

def getServices():
  #read in the config file for the service list
  f = open("../config/services.csv", "r")
  services = f.read().split(",")
  return services

def getServicePcapMap():
  #Mapping to service -> pcap
  d =  {
  "service": ["example.pcap"]
  }
  d.clear()
  file = open("../config/mapping.csv", "r")
  mappings = file.read().split("\n")
  #Adding the dictionary Key (Service) to Values (Array of pcaps)
  for y in mappings:
    x = y.split(",")
    d.update( {x[0] : x[1::]} )

  return d

def load():
  return

def getPcaps():
  #read in the pcaps
  pcaps = os.listdir(path='pcap/')
  return pcaps
# mappings = getServicePcapMap()
# honeypot = honeypot.Honeypot()
# logger = logger.Logger()



def runPcaps(d, interface, selected, selectedPcaps):
  successFlag = True
  #get the current source IP from the testTools file
  CURRENT_SOURCE_IP = test_tools.getCurrentIP(interface)
  pcapCount = 0
  for service in d:
    selected[service] = []
    for pcap in d[service]:
      #selected Pcaps is the entire lsit of pcaps
      #.get() == 1 checks if the pcap is selected
      if(selectedPcaps[pcapCount].get() == 1):
        logging.info("=========================================================================================\n RUNNING " + str(selectedPcaps[pcapCount]) + " \n")
        pcapDict = test_tools.getPcapIps()
        PREVIOUS_SOURCE_IP = test_tools.getPreviousSource(pcap, pcapDict)
        PREVIOUS_DESTINATION_IP = test_tools.getPreviousDestination(pcap, pcapDict)
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