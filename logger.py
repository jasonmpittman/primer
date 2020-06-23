import primer
import primerFacade
import honeypot
import testTools
import primerGUI
import logging
import time
import os 
import subprocess
import sys

def getPcaps():
  #read in the pcaps
  pcaps = os.listdir(path='pcap/')
  return pcaps

#set up the logger
logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO, filename = time.strftime("my-%Y-%m-%d.log"))
sys.stdout = open('logs/%Y-%m-%d-%s.log', 'w')
sys.stderr = open('logs/%Y-%m-%d-%s.log', 'w')
  