# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:49:51 2019

@author: Sumukh Vaidya, Dept of Physics, IIT Bombay
"""
import visa
import time
import numpy as np
import pyautogui
from struct import unpack
import csv
import functions
import string


#functions.togglechannel(4)

# SECTION 1: COMM INITIATION, DO NOT TOUCH
#This section initiates communication with DSO, and  creates an object, [scope] that enables measurements
resources=visa.ResourceManager() #find if DSO is connected
if len(resources.list_resources())==0:
    print('Connection Error: No devices Available')
else:
    scopename=resources.list_resources()[0]  # Name the DSO
scope=resources.open_resource(scopename) # Create the measurement object
time.sleep(2) #Give it time to settle
pyautogui.click(315,750) #To activate the ArbStudio Window . Super essential to include this line
time.sleep(2)
# SECTION 1 OVER ##################################################

