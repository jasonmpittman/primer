import logging
import datetime
import sys

class Primer():
  _pcaps()
  _networking()
  _primerEngine()
  _mainForm()

  def main():
    #set up the logger
    logFileName = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.log'
    logFilePath = '../logs/'+ logFileName
    open(logFilePath, 'w')
    sys.stdout = open(logFilePath, 'w')
    sys.stderr = open(logFilePath, 'w')
    logging.basicConfig(filename=logFilePath,level=logging.DEBUG)
    self._pcaps = pcaps()
    self._networking = networking()
    self._primerEngine = primerEngine()
    self._mainForm = mainform()
    return

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

  def getPcaps():
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps

main()
