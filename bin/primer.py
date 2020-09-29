import logging
import datetime
import sys
import os

class Primer():
  _pcaps()
  _networking()
  _primerEngine()
  _mainForm()

  def main():
    #set up the logger
    #folder YearMonthDay
    os.mkdir("../logs/" + datetime.datetime.now().strftime("%Y%m%d"))
    #create the log file in the new monthday folder
    logFileName = datetime.datetime.now().strftime("%Y%m%d") + "/" + datetime.datetime.now().strftime("%H%M%S")+'.log'
    logFilePath = '../logs/'+ logFileName
    open(logFilePath, 'w')
    sys.stdout = open(logFilePath, 'w')
    sys.stderr = open(logFilePath, 'w')
    logging.basicConfig(filename=logFilePath,level=logging.DEBUG)

    #init the primer objects
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
    #create dictionary with key of service and value of name
    #pcapInfo[1] mapped to pcapInfo[0] (1 is service, 0 is name)
    d =  {
    "service": ["example.pcap"]
    }
    d.clear()
    file = open("../config/pcapInfo.csv", "r")
    mappings = file.read().split("\n")
    #Adding the dictionary Key (Service) to Values (Array of pcaps)
    for y in mappings:
      x = y.split(",")
      d.update( {x[1] : x[0::]} )

    return d

  def getPcaps():
    #read in the pcaps
    pcaps = os.listdir(path='pcap/')
    return pcaps

main()
