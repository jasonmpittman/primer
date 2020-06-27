import primerGUI as gui
import logging
import datetime

def main():
  #set up the logger
  logFileName = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.log'
  logFilePath = '../logs/'+ logFileName
  open(logFileName, 'w')
  logging.basicConfig(filename=logFilePath,level=logging.DEBUG)
  gui.run()
  # #BEFORE MAKING WINDOW -- LOOK INTO FILESYSTEM AND GRAB DATA
  # print("here")
  # selectedServices = []
  # honeypotIP, pcaps = None, None
main()
#sudo tcpreplay-edit -i (network socket) -S (previous source ip):(new source ip) -D (previous dest ip):(new dest ip) (name of pcap file to replay)
# #store values of the form
# #if selected services is empty bring up a popup - oops! select a service.
# self.parentApp.selectedServices = self.serviceBox.get_selected_objects()
# self.parentApp.honeypotInfo = self.honeypotInfoBox.values
