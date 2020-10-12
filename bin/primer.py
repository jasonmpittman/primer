import logging
import datetime
import sys
import os
import tkinter as tk
import pcaps, networking, primer_engine, main_form

class Primer():
  def __init__(self):
    self.make_logger()
    self.__pcaps = pcaps.pcaps(logging)
    self.__networking = networking.Networking(logging)
    self.__primerEngine = primer_engine.PrimerEngine(self.__networking, logging)
    #self.__root = tk.Tk()
    #self.__mainForm = main_form.MainForm(master=self.__root)


  def make_logger(self):
    #Creates the YearMonthDay directory
    os.makedirs("../logs/" + datetime.datetime.now().strftime("%Y%m%d"), exist_ok=True)

    #Creates the log file in the YearMonthDay directory
    logFileName = datetime.datetime.now().strftime("%Y%m%d") + "/" + datetime.datetime.now().strftime("%H%M%S")+'.log'
    logFilePath = '../logs/'+ logFileName
    open(logFilePath, 'w')
    sys.stdout = open(logFilePath, 'w')
    sys.stderr = open(logFilePath, 'w')
    logging.basicConfig(filename=logFilePath,level=logging.DEBUG)

  def getServicePcapMap(self):
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

  def getPcaps(self):
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps

  def runPcaps(self, pcapName, honeypotIP, interface):
      self.__networking.setHostIpRuntime(interface)
      self.__networking.setTarget_ip(honeypotIP)
      self.__primerEngine.run(pcapName)

  def getInterfaceList(self):
      return self.__networking.interfaces()

  def main(self):
    #gui setup
    '''
    if os.environ.get('DISPLAY','') == '':
      logging.info('no display found. Using non-interactive Agg backend')
      os.environ.__setitem__('DISPLAY', ':0.0')
    '''
    #self.__mainForm.mainloop()
    #pcap file, honeypotIP, interface
    #Call run
    print(len(sys.argv))
    if len(sys.argv) != 4:
      print("Correct syntax: python3 primer.py <path topcap file name> <honeypot ip> <interface> ")
    else:
      self.runPcaps(sys.argv[1],sys.argv[2],sys.argv[3])

  def getServices(self):
    #read in the config file for the service list
    #f = open("../config/services.csv", "r")
    #services = f.read().split(",")
    #return services
    return


if __name__ == "__main__":
  primer = Primer()
  primer.main()