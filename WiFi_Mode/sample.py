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

#Connect to camera 1 and send locate command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0", True) == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/locate?p=1") == False:
        print("Sending command failed.")


#Switch connection to camera 2 and send locate command
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0", True) == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/locate?p=1") == False:
        print("Sending command failed.")


#Switch connection back to camera 1 and send stop locate command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/locate?p=0") == False:
        print("Sending command failed.")

#Switch connection back to camera 2 and send stop locate command
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/locate?p=0") == False:
        print("Sending command failed.")

#Switch to cam 1 and set the current system date and time as camera date and time
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
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/setup/date_time?p=" + cDateGPFormat) == False:
        print("Sending command failed.")

#Switch to cam 2 and set the current system date and time as camera date and time
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
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/setup/date_time?p=" + cDateGPFormat) == False:
        print("Sending command failed.")

#Switch connection back to cam 1 and switch mode to video
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/mode?p=0") == False:
        print("Sending command failed.")

#Switch connection back to cam 2 and switch mode to video
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/mode?p=0") == False:
        print("Sending command failed.")

#Switch back to cam1 and send start recording command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/shutter?p=1") == False:
        print("Sending command failed.")


#Switch connection back to cam2 and send start recording command
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
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


#Switch connection back to cam2 and send stop recording command
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


#Switch back to cam1 and send sleep command
if gp_wifi.createNewConnection("/etc/cam1.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25232893", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25232893")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/sleep") == False:
        print("Sending command failed.")


#Switch connection back to cam2 and send sleep command
if gp_wifi.createNewConnection("/etc/cam2.conf", "wlp4s0") == False:
    print("Could not connect to Camera. Exiting..")
    sys.exit()

if gp_wifi.checkIfConnected("GP25730195", 0.0, 0) == False:
    print("Connection could not be established with the Camera access point. Exiting..")
    sys.exit()
else:
    print("Connected to GP25730195")
    if gp_wifi.sendCommand("http://10.5.5.9/gp/gpControl/command/system/sleep") == False:
        print("Sending command failed.")