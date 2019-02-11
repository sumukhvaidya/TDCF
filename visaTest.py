# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:49:51 2019

@author: hodlab
"""
import functions
import pyautogui
import time 

pyautogui.click(315,750) #To activate the ArbStudio Window . Super essential to include this line

#v=[0,-1,-2,-3]
#for i in v:
#    functions.setvoltage(0,i,1)
#    time.sleep(5)

#functions.settriggerdelay(200,2)
#functions.setvoltage(2,-1,1)

functions.togglechannel(4)
