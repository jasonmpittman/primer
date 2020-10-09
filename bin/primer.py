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
    self.__root = tk.Tk()
    self.__mainForm = main_form.MainForm(master=self.__root)


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

  def main(self):
    #gui setup
    if os.environ.get('DISPLAY','') == '':
      logging.info('no display found. Using non-interactive Agg backend')
      os.environ.__setitem__('DISPLAY', ':0.0')
    self.__mainForm.mainloop()



  def getServices(self):
    #read in the config file for the service list
    #f = open("../config/services.csv", "r")
    #services = f.read().split(",")
    #return services
    return


if __name__ == "__main__":
  primer = Primer()
  primer.main()