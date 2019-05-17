import sys
import gp_wifi
from datetime import datetime


#the camera object used to store the information of the cameras as read from the 
#config file.
Cameras = []
gp_wifi.cameraConfig.readConfig(Cameras)
print(str(len(Cameras)) +  " Camera(s) configured.")

#This function always needs to be called in the beginning. 
if gp_wifi.initialize() == False:
    print("Initialization failed. Exiting..")
    sys.exit()

#Create connection with cam1
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
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
    #do time sync
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/setup/date_time?p=" + cDateGPFormat) == False:
        print("Sending command failed.")

    #switch to video mode.
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/mode?p=0") == False:
        print("Sending command failed.")

    #start recording
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=1") == False:
        print("Sending command failed.")

#switch connection to cam2
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    cDate = datetime.now()
    cDateGPFormat = "%" + '{:x}'.format(cDate.year - 2000) + \
                    "%" + '{:x}'.format(cDate.month) + \
                    "%" + '{:x}'.format(cDate.day) + \
                    "%" + '{:x}'.format(cDate.hour) + \
                    "%" + '{:x}'.format(cDate.minute) + \
                    "%" + '{:x}'.format(cDate.second)
    #time sync
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/setup/date_time?p=" + cDateGPFormat) == False:
        print("Sending command failed.")

    #switch to video mode.
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/mode?p=0") == False:
        print("Sending command failed.")

    #start recording.
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=1") == False:
        print("Sending command failed.")

#Switch back to cam1 and send stop recording command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=0") == False:
        print("Sending command failed.")

#Switch back to cam2 and send stop recording command
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=0") == False:
        print("Sending command failed.")
