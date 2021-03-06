# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:35:47 2019
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

#Section 2: Data acquisition: Data wil be saved as follows:####################################################
# tek0010.csv: Dark data file, data files for light data acquisition will be tek0011.csv onwards.
inputfile=open('./configuration/tdconfig.txt','r')
x=[line.split(' ') for line in inputfile.readlines()]
print (x[0][0])

saveindex=10 #Setting up a variable to save data files. Saved files start from tek0010.csv onwards.
savedelimiter=''

#Dark data acquisition before time variation###################################################
functions.settriggerdelay(float(x[0][0]),1)#Set delay as first entry of the time vector
functions.togglechannel(2) #Turn laser off for dark data acquisition
functions.savedatacsv(scope,1,savedelimiter.join(('./DATA/tek00', str(saveindex))))
saveindex+=1
functions.togglechannel(2)#Turn the laser back on

#Data acquisition in light by time variation#####################################################
for td in x[0]:
    #Light data
    functions.settriggerdelay(float(td),1)
    functions.savedatacsv(scope,1,savedelimiter.join(('./DATA/tek00', str(saveindex))))
    saveindex+= 1

