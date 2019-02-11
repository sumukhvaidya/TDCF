# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:57:51 2019


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

#Measurements:
#functions.settriggerdelay(1000,1)
#functions.settriggerdelay(1000,2)

inputfile=open('vpreconfig.txt','r')
x=[line.split(' ') for line in inputfile.readlines()]
print (x[0][0])

saveindex=10 #Setting up a variable to save data files. Saved files start from tek0001.csv onwards.
savedelimiter=''
for voltage in x[0]:
    #Light data
    functions.setvoltage(float(voltage),-2,1)
    functions.savedatacsv(scope,1,savedelimiter.join(('./DATA/tek00', str(saveindex))))
    saveindex+= 1
    #DARK data saving
    functions.togglechannel(2) #Turn laser off for dark data 
    functions.savedatacsv(scope,1,savedelimiter.join(('./DATA/tek00', str(saveindex))))
    saveindex+=1
    functions.togglechannel(2)#Turn laser on for light data
    time.sleep(1)

#pyautogui.click(1220,110)
#pyautogui.typewrite(str(x[0][0]),interval=0.1)