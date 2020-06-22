import primer.py
import primerFacade.py
import honeypot.py
import testTools.py
import primerGUI.py

def getPcaps:
  #read in the pcaps
  pcaps = os.listdir(path='pcap/')
  return pcaps

    #set up the logger
  logger = logging.getLogger(__name__)
  logging.basicConfig(level = logging.INFO, filename = time.strftime("my-%Y-%m-%d.log"))
  sys.stdout = open('logs/%Y-%m-%d-%s.log', 'w')
  sys.stderr = open('logs/%Y-%m-%d-%s.log', 'w')
  