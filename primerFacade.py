import primer.py
import honeypot.py
import testTools.py
import logger.py
import primerGUI.py

def getServices:
  #read in the config file for the service list
  f = open("config/services.csv", "r")
  services = f.read().split(",")
  return services

def getServicePcapMap(self):
  #Mapping to service -> pcap
  d =  {
  "service": ["example.pcap"]
  }
  d.clear()
  file = open("config/mapping.csv", "r")
  mappings = file.read().split("\n")
  #Adding the dictionary Key (Service) to Values (Array of pcaps)
  for y in mappings:
    x = y.split(",")
    d.update( {x[0] : x[1::]} )
  return mappings

mappings = self.getServicePcapMap()
honeypot = honeypot.Honeypot()
logger = logger.Logger()