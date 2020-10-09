import logging
import datetime
import sys
import os
import tkinter as tk
import pcaps, networking, primer_engine, main_form

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

    #gui setup
    if os.environ.get('DISPLAY','') == '':
      logging.info('no display found. Using non-interactive Agg backend')
      os.environ.__setitem__('DISPLAY', ':0.0')
    root = tk.Tk()
    self._mainForm = mainform.mainform(master=root)
    #app = mainform(master=root)
    self._mainForm.mainloop()



  def getServices(self):
    #read in the config file for the service list
    #f = open("../config/services.csv", "r")
    #services = f.read().split(",")
    #return services
    return


primer = Primer()
