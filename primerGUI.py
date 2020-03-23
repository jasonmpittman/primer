from tkinter import *
from tkinter import ttk
import os 
import socket
import netifaces as ni
import logging
import time
import subprocess

#if no display is found use :0.0
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#BEFORE MAKING WINDOW -- LOOK INTO FILESYSTEM AND GRAB DATA
selectedServices = []
honeypotIP, pcaps = None, None
PREVIOUS_SOURCE_IP = "172.16.0.137"
PREVIOUS_DESTINATION_IP = "172.16.0.201"
#read in the config file for the service list
f = open("config/services.csv", "r")
services = f.read().split(",")

#read in the pcaps
pcaps = os.listdir(path='pcap/')

#Mapping to service -> pcap
d =  {
"service": ["example.pcap"]
}
d.clear()
f = open("config/mapping.csv", "r")
mappings = f.read().split("\n")

#Adding the dictionary Key (Service) to Values (Array of pcaps)
for y in mappings:
  x = y.split(",")
  d.update( {x[0] : x[1::]} )

#getting possible net interfaces for the current ip
interfaces_list = ni.interfaces()

root = Tk()
frame_a = Frame()
frame_b = Frame()

serviceCounter = 0
pcapCount = 0
selectedServices = []
selectedPcaps = []
for service in d:
  l = Label(master=frame_a, text=service)
  l.pack()
  for pcap in d[service]:
    a = IntVar()
    selectedPcaps.append(a)
    c = Checkbutton(master=frame_a, text=pcap, variable=selectedPcaps[pcapCount])
    c.pack()
    pcapCount += 1

l = Label(master=frame_b, text="HONEYPOT IP:")
l.pack()
entry = Entry(master=frame_b, fg="yellow", bg="blue", width=50)
entry.pack()

interface = StringVar(root)
interfaceMenu = ttk.Combobox(master=frame_b, textvariable=interface, values=interfaces_list)
interfaceMenu.pack()

def handle_click(event):
  #set up the logger
  logger = logging.getLogger(__name__)
  logging.basicConfig(level = logging.INFO, filename = time.strftime("my-%Y-%m-%d.log"))


  #Mapping to service -> pcap
  selected =  {
  "service": ["example.pcap"]
  }
  selected.clear()  

  #retrieve info from fields
  honeypotIP = entry.get()
  interface = interfaceMenu.get()
  CURRENT_SOURCE_IP = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
  pcapCount = 0
  for service in d:
    selected[service] = []
    for pcap in d[service]:
      if(selectedPcaps[pcapCount].get() == 1):
        selected[service].append(pcap)
        command = "sudo tcpreplay-edit -i " + interface + " -S "  + PREVIOUS_SOURCE_IP + ":" + CURRENT_SOURCE_IP + " -D " + PREVIOUS_DESTINATION_IP + ":" + honeypotIP + " " + pcap
        process = subprocess.check_output(['bash', '-c', command])
        logging.info(command) 
      pcapCount += 1

  print(command)

button = Button(master=frame_b, text="RUN")

button.pack()
button.bind("<Button-1>", handle_click)




frame_a.pack(fill=BOTH, side=LEFT)
frame_b.pack(fill=BOTH, side=RIGHT)
root.mainloop()


#sudo tcpreplay-edit -i (network socket) -S (previous source ip):(new source ip) -D (previous dest ip):(new dest ip) (name of pcap file to replay)
# #store values of the form
# #if selected services is empty bring up a popup - oops! select a service.
# self.parentApp.selectedServices = self.serviceBox.get_selected_objects()     
# self.parentApp.honeypotInfo = self.honeypotInfoBox.values