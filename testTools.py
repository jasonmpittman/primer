import primer.py
import primerFacade.py
import honeypot.py
import logger.py
import primerGUI.py

#getting possible net interfaces for the current ip
interfaces_list = ni.interfaces()

def getCurrentIP(interface):
    return ni.ifaddresses(interface)[ni.AF_INET][0]['addr']