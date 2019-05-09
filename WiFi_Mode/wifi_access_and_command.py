
#connection and send the command specified in the configuration and then proceed
#to do the same thing with any more goPro's which are configured.

#First lets loop over the entire configuration file and store the data and
#commands in convienient data structures.

import subprocess
import time
import urllib2

sleep_time = 5 #seconds

class Camera:
    name = ''
    password = ''
    commands = []

Cameras = []

conf = open("goProAccessPt.conf", mode='r')
confLines = conf.readlines()

tempCamera = Camera()

for x in range(0, len(confLines)):
    if confLines[x][0:3] == '[GP': #Start of configuration
        if len(tempCamera.commands) > 0:
            Cameras.append(tempCamera)
            tempCamera = Camera()
            tempCamera.commands = []
    else:
        splitconf = confLines[x].split('=') #Read the name
        if splitconf[0].replace(" ", "") == 'Access_pt_name':
            tempCamera.name = splitconf[1].replace(" ", "").replace("\n", "")
        elif splitconf[0].replace(" ", "") == 'Access_pt_password':
            tempCamera.password = splitconf[1].replace(" ", "").replace("\n", "")
        else:
            command = confLines[x].replace(" ", "").replace("\n", "")
            if len(command) > 0 :
                (tempCamera.commands).append(command)
Cameras.append(tempCamera)

conf.close()

#Now iterate over the Cameras, attempt connection with the access point created by
#the indvidual cameras and send the commands

for x in range(0, len(Cameras)):
    connect_command = "nmcli dev wifi connect " + Cameras[x].name + " password " + Cameras[x].password
    print (connect_command)
    out =  subprocess.check_output(connect_command, stderr=subprocess.STDOUT, shell=True)
    print(out)
    time.sleep(sleep_time * 2)
    check_command = "iwgetid -r"
    out =  subprocess.check_output(check_command, stderr=subprocess.STDOUT, shell=True)
    if out.replace(" ", "").replace("\n", "") == Cameras[x].name:
        print("Camera Connected")
        for y in range(0, len(Cameras[x].commands)):
            print("Sending command: ", Cameras[x].commands[y], " to camera: ", x)
            urllib2.urlopen(Cameras[x].commands[y])
            time.sleep(sleep_time)


#References :
#1. https://askubuntu.com/questions/16584/how-to-connect-and-disconnect-to-a-network-manually-in-terminal
#2. https://askubuntu.com/questions/117065/how-do-i-find-out-the-name-of-the-ssid-im-connected-to-from-the-command-line
#3. https://docs.python.org/3/library/subprocess.html#subprocess.check_output
#4. https://docs.python.org/3/library/dataclasses.html
#5. https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517
