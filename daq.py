# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:22:31 2019


@author: Sumukh Vaidya, Dept of Physics, IIT Bombay
"""
import visa
import time
import numpy as np
import pyautogui
from struct import unpack
import csv
import functions

# SECTION 1: COMM INITIATION
#This section initiates communication with DSO, and  creates an object, [scope] that enables measurements
resources=visa.ResourceManager()
if len(resources.list_resources())==0:
    print('Connection Error: No devices Available')
else:
    scopename=resources.list_resources()[0]    
scope=resources.open_resource(scopename)
time.sleep(2) #Give it time to settle
pyautogui.click(315,750) #To activate the ArbStudio Window . Super essential to include this line
time.sleep(0.5)
# SECTION 1 OVER ##################################################


# SECTION 2: MEASUREMENTS
# Use input here to make measurements

functions.settriggerdelay(400,1)
time.sleep(0.2)
functions.setvoltage(2,-1,1)
time.sleep(0.2)
functions.savedatacsv(scope,1,'./DATA/cde')

