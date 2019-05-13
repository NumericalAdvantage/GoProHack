import sys
import os
import signal
import subprocess
import time
import cameraConfig

def initialize():
    try:
        subprocess.call("systemctl stop NetworkManager", stderr=subprocess.STDOUT, shell=True)
        return True
    except Exception as exc:
        print(exc)
        return False

def createNewConnection(camera_config_file_path, interface_name, first_connect = False):
    connect_command = "wpa_supplicant -B -D nl80211 -i " + interface_name + " -c " + camera_config_file_path
    try:
        subprocess.call("killall wpa_supplicant", stderr=subprocess.STDOUT, shell=True)
        subprocess.call(connect_command, stderr=subprocess.STDOUT, shell=True)
        if first_connect == True:
            subprocess.call("dhclient " + interface_name, stderr=subprocess.STDOUT, shell=True)
        return True
    except Exception as exc:
        print(exc)
        return False

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

def sendCommand(command):
    try:
        print("Sending command: " + command)
        subprocess.call("curl -v " + command, shell=True)
        return True
    except Exception as exc:
        print(exc)
        print("Sending command " + command + " failed." )
        return False
