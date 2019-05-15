#This is another sample script and it performs the following:
#- connect to GoPro
#- sync time
#- check live view (for 10 seconds)
#- start recording (record for 10 seconds)
#- stop recording

import sys
import gp_wifi
from datetime import datetime
import subprocess
import os
import signal
import time

#the camera object used to store the information of the cameras as read from the 
#config file.
Cameras = []
gp_wifi.cameraConfig.readConfig(Cameras)
print(str(len(Cameras)) +  " Camera(s) configured.")

#This function always needs to be called in the beginning. 
if gp_wifi.initialize() == False:
    print("Initialization failed. Exiting..")
    sys.exit()

#Connect to camera 1 and send locate command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0", True) == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    cDate = datetime.now()
    cDateGPFormat = "%" + '{:x}'.format(cDate.year - 2000) + \
                    "%" + '{:x}'.format(cDate.month) + \
                    "%" + '{:x}'.format(cDate.day) + \
                    "%" + '{:x}'.format(cDate.hour) + \
                    "%" + '{:x}'.format(cDate.minute) + \
                    "%" + '{:x}'.format(cDate.second)
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/setup/date_time?p=" + cDateGPFormat) == False:
        print("Sending command failed.")

    #Check live view. 
    out = subprocess.Popen("/home/rgh/anaconda3/bin/python GoProStream.py", stdout=subprocess.PIPE, 
                              shell=True, preexec_fn=os.setsid)
    time.sleep(10)
    os.killpg(os.getpgid(out.pid), signal.SIGTERM)

    #Switch to video mode
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/mode?p=0") == False:
        print("Sending command failed.")

    #Start recording    
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=1") == False:
        print("Sending command failed.")

    time.sleep(10)

    #Stop recording
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=0") == False:
        print("Sending command failed.")
