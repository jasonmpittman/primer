import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import testTools
import primerFacade
import logging

class mainform(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.grid()
    self.create_widgets()
    self.logFile = ""


  def create_widgets(self):
    #create the pcap chooser
    self.title = tk.Label(master=self, text="Select a PCAP to run:", font='Helvetica 12 bold')
    self.title.grid(row=0, column=1)
    #get the dictionary of services --> pcaps
    servicePcapMap = primer.getServicePcapMap()


    counter = 1
    pcapCount = 0
    selectedServices = []
    self.selectedPcaps = []
    #create the checklist of services and their associated pcaps for the user to select
    for service in servicePcapMap:
      #make header of service
      self.l = tk.Label(master=self, text=service, font='Helvetica 10 bold')
      self.l.grid(row=counter, column=1)

      for pcap in servicePcapMap[service]:
        a = tk.IntVar()
        self.selectedPcaps.append(a)
        self.c = tk.Checkbutton(master=self, text=pcap, variable=self.selectedPcaps[pcapCount])
        self.c.grid(row=counter + 1, column=1)
        pcapCount += 1
        counter += 1

      counter += 1

    #create the honeypot entry and label info
    self.honeyPotLabel = tk.Label(master=self, text="HONEYPOT IP:", font='Helvetica 12 bold')
    self.honeyPotLabel.grid(row=0, column=2)

    self.honeyPotEntry = tk.Entry(master=self, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
    self.honeyPotEntry.grid(row=1, column=2)

    #create the network interface chooser
    self.netiLabel = tk.Label(master=self, text="CONNECTION INTERFACE:", font='Helvetica 12 bold')
    self.netiLabel.grid(row=0, column=4)

    interfaces_list = primer.getInterfaceList()
    interface = tk.StringVar()
    self.interfaceMenu = ttk.Combobox(master=self, textvariable=interface, values=interfaces_list)
    self.interfaceMenu.grid(row=1, column=4)

    #create the run button
    self.run = tk.Button(self)
    self.run["text"] = "RUN"
    self.run["command"] = primer.handle_run()
    self.run.grid(row=4, column=2)

    #create the add button
    self.add = tk.Button(self)
    self.add["text"] = "Add a PCAP"
    self.add["command"] = self.open_New_Window
    self.add.grid(row=6, column=2)



  def open_New_Window(self):
    self.newWindow = tk.Toplevel(self.master)
    self.newWindow.title("Add a Pcap")
    self.newWindow.geometry("200x200")
    self.newWindow.grid()

    self.label = tk.Label(self.newWindow, text = "New PCAP Entry")
    self.label.grid(row=0, column=0)

    self.fileLabel = tk.Label(self.newWindow, text = "Pcap File:")
    self.fileLabel.grid(row=1, column=0)
    self.fileButton = tk.Button(self.newWindow, text = "Click to browse...", command=self.file_chooser)
    self.fileButton.grid(row=2, column=0)

    self.newSourceLabel = tk.Label(self.newWindow, text = "Pcap Source IP:")
    self.newSourceLabel.grid(row=3, column=0)
    self.newSourceEntry = tk.Entry(self.newWindow, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
    self.newSourceEntry.grid(row=4, column=0)

    self.newDestinationLabel = tk.Label(self.newWindow, text = "Pcap Destination IP:")
    self.newDestinationLabel.grid(row=5, column=0)
    self.newDestinationEntry = tk.Entry(self.newWindow, fg="yellow", bg="blue", width=30, font = 'Helvetica 10 bold')
    self.newDestinationEntry.grid(row=6, column=0)

    self.closeButton = tk.Button(self.newWindow, text = "add", command=self.close_Add)
    self.closeButton.grid(row=7, column=0)

  def close_Add(self):
    self.newWindow.destroy()

  def file_chooser(self):
    #make this actually work to add a pcap to the config file eventually
    self.newPcapFile = tk.filedialog.askopenfile(parent=self.newWindow, initialdir=os.getcwd(), title="Please select a Pcap", filetypes = [('pcap files', '.pcap')])
    print(self.newPcapFile)
    self.fileLabel.text=self.newPcapFile.name
    self.fileLabel.grid(row=1, column=0)

  def handle_run(self):
    #Mapping to service -> pcap
    selected =  {
      "service": ["example.pcap"]
    }
    selected.clear()

    servicePcapMap = primer.getServicePcapMap()
    #retrieve info from fields
    honeypotIP = self.honeyPotEntry.get()
    interface = self.interfaceMenu.get()

    success = primer.runPcaps(servicePcapMap, honeypotIP, interface, self.selectedPcaps)

    #After running --> have a popup telling if it was successful or not
    if success:
      tk.messagebox.showinfo("Primer", "Command Ran Successfully")
    else:
      tk.messagebox.showinfo("Primer", "Pcaps ran with errors - see log file for details.\nLog located at: " + self.logFile)
