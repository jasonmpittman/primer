from tkinter import *
from tkinter import ttk
import os
import subprocess
import primerFacade
import testTools
import socket
import netifaces as ni
# import honeypot as honeypot
# import testTools as tools
# import logger as logger
def run():
  #if no display is found use :0.0
  if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
  root = Tk()
  d = primerFacade.getServicePcapMap()
  l = Label(master=root, text="Select a PCAP to run:", font='Helvetica 12 bold')
  l.grid(row=0, column=0)
  counter = 1
  pcapCount = 0
  selectedServices = []
  selectedPcaps = []
  for service in d:
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

  button = Button(master=root, text="RUN", command=handle_click(entry, interfaceMenu, d, selectedPcaps))
  button.grid(row=4, column=2)
  root.mainloop()

def handle_click(entry, interfaceMenu, d, selectedPcaps):
  #Mapping to service -> pcap
  print("here")
  selected =  {
    "service": ["example.pcap"]
  }
  selected.clear()
  #retrieve info from fields
  honeypotIP = entry.get()
  primerFacade.honeypotIP = entry.get()
  interface = interfaceMenu.get()
  #get the current source IP from the testTools file
  CURRENT_SOURCE_IP = testTools.getCurrentIP(interface)
  print(d)
  pcapCount = 0
  for service in d:
    selected[service] = []
    for pcap in d[service]:
      print(pcap)
      if(selectedPcaps[pcapCount].get() == 1):
        PREVIOUS_SOURCE_IP = testTools.getPreviousSource(pcap)
        PREVIOUS_DESTINATION_IP = testTools.getPreviousDestination(pcap)
        selected[service].append(pcap)
        command = "sudo tcpreplay-edit -i " + interface + " -S "  + PREVIOUS_SOURCE_IP + ":" + CURRENT_SOURCE_IP + " -D " + PREVIOUS_DESTINATION_IP + ":" + honeypotIP + " " + pcap
        print(command)
        process = subprocess.check_output(['bash', '-c', command])
        print(command)
      pcapCount += 1
