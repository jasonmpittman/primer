# import honeypot
# import logger


def getServices():
  #read in the config file for the service list
  f = open("config/services.csv", "r")
  services = f.read().split(",")
  return services

def getServicePcapMap():
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

  return d

def getPcaps():
  #read in the pcaps
  pcaps = os.listdir(path='pcap/')
  return pcaps
# mappings = getServicePcapMap()
# honeypot = honeypot.Honeypot()
# logger = logger.Logger()
