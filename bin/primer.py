import logging
import datetime
import sys
import os
import tkinter as tk
import pcaps, networking, primer_engine, mainform

class Primer():
  def __init__(self):
    self.__pcaps = None
    self.__networking = None
    self.__primerEngine = None
    self.__mainForm = None
    self.main()

  def main(self):
    #set up the logger
    #folder YearMonthDay
    #try:
    os.makedirs("../logs/" + datetime.datetime.now().strftime("%Y%m%d"), exist_ok=True)
    #except Exception e:

    #create the log file in the new monthday folder
    logFileName = datetime.datetime.now().strftime("%Y%m%d") + "/" + datetime.datetime.now().strftime("%H%M%S")+'.log'
    logFilePath = '../logs/'+ logFileName
    open(logFilePath, 'w')
    sys.stdout = open(logFilePath, 'w')
    sys.stderr = open(logFilePath, 'w')
    logging.basicConfig(filename=logFilePath,level=logging.DEBUG)

    #init the primer objects
    self._pcaps = pcaps.pcaps(logging)
    self._networking = networking.Networking(logging)
    self._primerEngine = primer_engine.PrimerEngine(self._networking, logging)
    root = tk.Tk()
    self._mainForm = mainform.mainform(logging, master=root)
    #app = mainform(master=root)
    self._mainForm.mainloop()
    #return

  def getServices(self):
    #read in the config file for the service list
    #f = open("../config/services.csv", "r")
    #services = f.read().split(",")
    #return services
    return

  def getServicePcapMap(self):
    #create dictionary with key of service and value of name
    #pcapInfo[1] mapped to pcapInfo[0] (1 is service, 0 is name)
    dict =  {
    "service": ["example.pcap"]
    }
    dict.clear()
    pcaps = self.__pcaps.getPcaps()
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

  def getPcaps(self):
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps

  def runPcaps(self, servicePcapMap, honeypotIP, interface, selectedPcaps):
      networking.sourceIp.setHostIpRuntime(interface)
      networking.setTarget_ip(honeypotIP)
      primerEngine.runPcaps(servicePcapMap, selectedPcaps)

  def getInterfaceList(self):
      return self.networking.interfaces()

primer = Primer()
