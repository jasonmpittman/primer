from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
import primerFacade
import testTools
import socket
import netifaces as ni
import logging
# import honeypot as honeypot
# import testTools as tools
# import logging as logging
def run(logFile):
  #if no display is found use :0.0
  if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
  root = Tk()

  #get the dictionary of services --> pcaps
  d = primerFacade.getServicePcapMap()

  l = Label(master=root, text="Select a PCAP to run:", font='Helvetica 12 bold')
  l.grid(row=0, column=0)

  counter = 1
  pcapCount = 0
  selectedServices = []
  selectedPcaps = []
  #create the checklist of services and their associated pcaps for the user to select
  for service in d:
    #make header of service
    l = Label(master=root, text=service, font='Helvetica 10 bold')
    l.grid(row=counter, column=0)

    for pcap in d[service]:
      a = IntVar()
      selectedPcaps.append(a)
      c = Checkbutton(master=root, text=pcap, variable=selectedPcaps[pcapCount])
      c.grid(row=counter + 1, column=0)
      pcapCount += 1
      counter += 1
    counter += 1

  l = Label(master=root, text="HONEYPOT IP:", font='Helvetica 12 bold')
  l.grid(row=0, column=2)

  entry = Entry(master=root, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
  entry.grid(row=1, column=2)

  l = Label(master=root, text="Connection Interface:", font='Helvetica 12 bold')
  l.grid(row=0, column=4)
  interface = StringVar(root)

  interfaces_list = testTools.getInterfaceList()
  interfaceMenu = ttk.Combobox(master=root, textvariable=interface, values=interfaces_list)
  interfaceMenu.grid(row=1, column=4)

  button = Button(master=root, text="RUN", command=lambda: handle_click(root, entry, interfaceMenu, d, selectedPcaps, logFile))
  button.grid(row=4, column=2)
  root.mainloop()
  logging.info('GUI launched successfully')



  

def handle_click(root, entry, interfaceMenu, d, selectedPcaps, logFile):
  #Mapping to service -> pcap
  selected =  {
    "service": ["example.pcap"]
  }
  selected.clear()
  #retrieve info from fields
  primerFacade.honeypotIP = entry.get()
  interface = interfaceMenu.get()
  #get the current source IP from the testTools file
  CURRENT_SOURCE_IP = testTools.getCurrentIP(interface)
  print(d, interface)
  logging.info('running following services/pcaps:' + str(selected))

  #run the selected Pcaps
  success = primerFacade.runPcaps(d, interface, selected, selectedPcaps)

  #After running --> have a popup telling if it was successful or not
  if success:
    messagebox.showinfo("Primer", "Command Ran Successfully")
  else:
    messagebox.showinfo("Primer", "Pcaps ran with errors - see log file for details.\nLog located at: " + logFile)