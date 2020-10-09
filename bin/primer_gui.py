from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import subprocess
import primer_facade
import test_tools
import socket
import netifaces as ni
import logging
import sys

def run(logFile):
  #if no display is found use :0.0
  if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
  root = Tk()

  #get the dictionary of services --> pcaps
  d = primer_facade.getServicePcapMap()

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

  interfaces_list = test_tools.getInterfaceList()
  interfaceMenu = ttk.Combobox(master=root, textvariable=interface, values=interfaces_list)
  interfaceMenu.grid(row=1, column=4)

  button = Button(master=root, text="RUN", command=lambda: handle_click(root, entry, interfaceMenu, d, selectedPcaps, logFile))
  button.grid(row=4, column=2)


  #ADDING PCAP SECTION
  pcapSectionHeader = Label(master=root, text="ADD A USER PCAP:", font='Helvetica 12 bold')
  pcapSectionHeader.grid(row=5, column=4)

  pcapFile = None
  pcapFileButton = Button(master=root, text="Pcap File", command=lambda: pcap_file(root, pcapFile, pcapFileButton))
  pcapFileButton.grid(row=6, column=4)

  servicePcapHeader = Label(master=root, text="Associated services (comma seperated)", font='Helvetica 12 bold')
  servicePcapHeader.grid(row=7, column=4)
  servEntry = Entry(master=root, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
  servEntry.grid(row=8, column=4)

  sourceLabel = Label(master=root, text="Pcap's source IP", font='Helvetica 12 bold')
  sourceLabel.grid(row=9, column=4)
  sourceEntry = Entry(master=root, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
  sourceEntry.grid(row=10, column=4)

  destLabel = Label(master=root, text="Pcap's destination IP", font='Helvetica 12 bold')
  destLabel.grid(row=11, column=4)
  destEntry = Entry(master=root, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
  destEntry.grid(row=12, column=4)

  addButton = Button(master=root, text="SAVE PCAP", command=lambda: add(root, pcapFile, pcapFileButton))
  addButton.grid(row=13, column=4)



  root.mainloop()
  logging.info('GUI launched successfully')


def pcap_file(root, pcapFile, pcapFileButton):
  pcapFile = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), title="Please select a Pcap", filetypes = [('pcap files', '.pcap')])
  pcapFileButton.text=pcapFile

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
  CURRENT_SOURCE_IP = test_tools.getCurrentIP(interface)
  logging.info('running following services/pcaps:' + str(selected))

  #run the selected Pcaps
  success = primer_facade.runPcaps(d, interface, selected, selectedPcaps)

  #After running --> have a popup telling if it was successful or not
  if success:
    messagebox.showinfo("Primer", "Command Ran Successfully")
  else:
    messagebox.showinfo("Primer", "Pcaps ran with errors - see log file for details.\nLog located at: " + logFile)