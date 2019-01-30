# Th screen Resolution is 1366x768
import pyautogui

#pyautogui.PAUSE=1  #Just a pausing command

def setvoltage(vbase, vpulse, ch):
    pyautogui.click(190,70) # Stop the current AFG run
    
    #Double click on Waveform Sequencer for specified channel no
    
    pyautogui.click(100,150+(ch-1)*65) 
    pyautogui.click(100,150+(ch-1)*65)
    
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
    
    pyautogui.click(930,640) # clicking ok button
    
    pyautogui.click(190,70) # Start the next AFG run
    return
