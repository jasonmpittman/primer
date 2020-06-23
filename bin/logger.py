import logging
import time
import os
import subprocess
import sys

class logger:
  logFileName = 'logs/%Y-%m-%d-%s.log'
  def __init__(self):
    #set up the logger
    logFileName = 'logs/%Y-%m-%d-%s.log'
    self = logging.basicConfig(filename=logFileName,level=logging.DEBUG)




