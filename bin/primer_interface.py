import primer 

class primer_interface():
  def __init__(self, primer):
    self.primer = primer

  def getServicePcapMap():
    #create dictionary with key of service and value of name
    #pcapInfo[1] mapped to pcapInfo[0] (1 is service, 0 is name)
    dict =  {
    "service": ["example.pcap"]
    }
    dict.clear()
    pcaps = primer.__pcaps.getPcaps()
    #Adding the dictionary Key (Service) to Values (Array of pcap names)
    #for a pcap object in the collection of pcaps
    for pcap in pcaps:
      if(dict.get(pcap.service() == None)):
        #if the service does not exist in our map, add it and the pcap
        dict.update( {pcap.service() : pcap.name()} )
      else:
        #if the service does exist in our map, just append thename to the name array
        dict.get(pcap.service()).append(pcap.name())
    return dict

  def getPcaps():
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps

  def runPcaps(servicePcapMap, honeypotIP, interface, selectedPcaps):
      networking.sourceIp.setHostIpRuntime(interface)
      networking.setTarget_ip(honeypotIP)
      primerEngine.runPcaps(servicePcapMap, selectedPcaps)

  def getInterfaceList():
      return primer.networking.interfaces()
