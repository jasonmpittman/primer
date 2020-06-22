from tkinter import *
from tkinter import ttk
import os 
import socket
import netifaces as ni
import logging
import time
import subprocess
import primerFacade.py
import honeypot.py
import testTools.py
import logger.py
import primerGUI.py



#BEFORE MAKING WINDOW -- LOOK INTO FILESYSTEM AND GRAB DATA
selectedServices = []
honeypotIP, pcaps = None, None
PREVIOUS_SOURCE_IP = "172.16.0.137"
PREVIOUS_DESTINATION_IP = "172.16.0.201"









#sudo tcpreplay-edit -i (network socket) -S (previous source ip):(new source ip) -D (previous dest ip):(new dest ip) (name of pcap file to replay)
# #store values of the form
# #if selected services is empty bring up a popup - oops! select a service.
# self.parentApp.selectedServices = self.serviceBox.get_selected_objects()     
# self.parentApp.honeypotInfo = self.honeypotInfoBox.values