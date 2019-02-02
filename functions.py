# Th screen Resolution is 1366x768
import pyautogui
import visa
import time
import numpy as np
from struct import unpack
import csv

#pyautogui.PAUSE=1  #Just a pausing command

def setvoltage(vbase, vpulse, ch):
    pyautogui.click(190,70) # Stop the current AFG run
    
    #Double click on Waveform Sequencer for specified channel no    
    pyautogui.click(100,150+(ch-1)*65) 
    pyautogui.click(100,150+(ch-1)*65)
#    time.delay(0.2)
    
    pyautogui.click(300,230) #Double click waveform  properties
    pyautogui.click(300,230)
    
    pyautogui.click(960,140) #Setting vpulse
    pyautogui.typewrite(str(vpulse),interval=0.1)
    pyautogui.typewrite('\n',interval=0.1)
    
    pyautogui.click(960,175) # Setting vbase
    pyautogui.typewrite(str(vbase),interval=0.1)
    pyautogui.typewrite('\n',interval=0.1)
    
    pyautogui.click(780,140) # Setting amplitude
    pyautogui.typewrite(str((vpulse-vbase)/2),interval=0.1)
    pyautogui.typewrite('\n',interval=0.1)
    
    pyautogui.click(930,640) # Clicking ok button
    
    pyautogui.click(190,70) # Start the next AFG run
    return


def settriggerdelay(t, ch): # t to be set in !NANOSECONDS!
    pyautogui.click(190,70) # Stop the current AFG run
    
    #Double click on Setting for specified channel no    
    pyautogui.click(100,130+(ch-1)*65) 
    pyautogui.click(100,130+(ch-1)*65)
#    time.delay(0.2)
    
    pyautogui.click(700,260) # Click Trigger Delay box
    pyautogui.typewrite(str(t),interval=0.1)# Enter time in NANOSECONDS
    pyautogui.typewrite('n',interval=0.1)
    pyautogui.typewrite('\n',interval=0.1)
    
    pyautogui.click(900,570) #  Clicking ok button
    
    pyautogui.click(190,70) # Start the next AFG run
    return


def savedatacsv(scope, ch, filename):
    s=""
    scope.write(s.join(('DATA:SOU CH',str(ch)))) #Set Data source Channel
    scope.write('DATA:WIDTH 1') # Set Data width
    scope.write('DATA:ENC RPB') # Set data encoding
    
    ymult = float(scope.query('WFMPRE:YMULT?')) # Pre-digitising level
    yzero = float(scope.query('WFMPRE:YZERO?')) # Offset, if any
    yoff = float(scope.query('WFMPRE:YOFF?')) # Related to trace position on screen
    xincr = float(scope.query('WFMPRE:XINCR?'))# Time increment in sampling (x axis)
    
    scope.write('CURVE?')
    data = scope.read_raw()
    headerlen = 2 + int(data[1])
    header = data[:headerlen]
    ADC_wave = data[headerlen:-1]
    
    ADC_wave = np.array(unpack('%sB' % len(ADC_wave),ADC_wave))
    
    Volts = (ADC_wave - yoff) * ymult  + yzero
    
    Time = np.arange(0, xincr * len(Volts), xincr)
    
    savefile=s.join((filename,'.csv'))
    with open(savefile,'w') as file:
        writer= csv.writer(file, delimiter=',')        
        for i in range(0,len(Time)):
            if i==0:
                writer.writerow(['Time','Volts'])
            else:
                writer.writerow([str(Time[i]),str(Volts[i])])    
    return