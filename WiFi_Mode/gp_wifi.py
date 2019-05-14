import sys
import os
import signal
import subprocess
import time
import cameraConfig

#Called only once during the beginning of the experiment. 
def initialize():
    try:
        #This step is necessary to ensure the network manager doesn't interfere with our operations.
        #If you find any other such thing which needs to be done only once per run of the 
        #experiment, you should ad those things here. 
        subprocess.call("systemctl stop NetworkManager", stderr=subprocess.STDOUT, shell=True)
        return True
    except Exception as exc:
        print(exc)
        return False

#Creates a new connection with the SSID and password defined in the config file using the wifi interface provided.
def createNewConnection(camera_config_file_path, interface_name, first_connect = False):
    connect_command = "wpa_supplicant -B -D nl80211 -i " + interface_name + " -c " + camera_config_file_path
    try:
        #wpa_suplicant doesn't work if there is a previous connection already exosting using it,
        #so first we kill the existing process (if any)
        subprocess.call("killall wpa_supplicant", stderr=subprocess.STDOUT, shell=True)
        subprocess.call(connect_command, stderr=subprocess.STDOUT, shell=True)
        if first_connect == True:
            #If a connection is made first time, this command should be fired
            subprocess.call("dhclient " + interface_name, stderr=subprocess.STDOUT, shell=True)
        return True
    except Exception as exc:
        print(exc)
        return False

#User can configure how many reattempts should be made before we "hang up". User also controls how long we "wait" 
#before successive connection check attempts. 
def checkIfConnected(CameraName, time_delay, number_of_retries):
    for _ in range(0, number_of_retries):
        try:
            out = subprocess.check_output("iwgetid -r", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
            if out.replace(" ", "").replace("\n", "") == CameraName:
                return True
            else:
                return False    
        except Exception as exc:
            print(exc)
            return False
        time.sleep(time_delay)

#Sends the command passed to it using cURL. 
def sendCommand(command):
    try:
        print("Sending command: " + command)
        subprocess.call("curl --verbose " + command, shell=True)
        return True
    except Exception as exc:
        print(exc)
        print("Sending command " + command + " failed." )
        return False
