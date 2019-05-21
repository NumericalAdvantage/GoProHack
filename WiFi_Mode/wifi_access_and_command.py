
#connection and send the command specified in the configuration and then proceed
#to do the same thing with any more goPro's which are configured.

#First lets loop over the entire configuration file and store the data and
#commands in convienient data structures.

import os
import signal
import subprocess
import time
from urllib.request import urlopen
import cameraConfig

sleep_time = 1 #seconds


#Now iterate over the Cameras, attempt connection with the access point created by
#the indvidual cameras and send the commands
def connectToCamerasAndSendTheCommands():
    for x in range(0, len(Cameras)):
        connect_command = "nmcli dev wifi connect " + Cameras[x].name + " password " + Cameras[x].password
        print (connect_command)
        out = subprocess.Popen(connect_command, stdout=subprocess.PIPE, 
                              shell=True, preexec_fn=os.setsid)
        os.killpg(os.getpgid(out.pid), signal.SIGTERM)  # Send the signal to all the process groups
        print(out)
        time.sleep(sleep_time * 2)
        check_command = "iwgetid -r"
        out =  subprocess.check_output(check_command, stderr=subprocess.STDOUT, shell=True)
        if out.replace(" ", "").replace("\n", "") == Cameras[x].name:
            print("Camera Connected")
            for y in range(0, len(Cameras[x].commands)):
                print("Sending command: ", Cameras[x].commands[y], " to camera: ", x)
                urlopen(Cameras[x].commands[y])
                time.sleep(sleep_time)



#connects to the camera which matches the index of cameras in the Cameras list.
def connectCamera(camIdx, delay):
    connect_command = "nmcli dev wifi connect " + Cameras[camIdx].name + " password " + Cameras[camIdx].password
    try:
        
        out = subprocess.Popen(connect_command, stdout=subprocess.PIPE, 
                               shell=True, preexec_fn=os.setsid)
        print("Attempting connection with ", Cameras[camIdx].name)
        
        out.wait()

        #os.killpg(os.getpgid(out.pid), signal.SIGTERM)

        if Cameras[camIdx].state == 0:
            print("Sending command: ", Cameras[camIdx].commands[3], " to ", Cameras[camIdx].name)
            urlopen(Cameras[camIdx].commands[3])
            Cameras[camIdx].state = 1
        elif Cameras[camIdx].state == 1:
            print("Sending command: ", Cameras[camIdx].commands[4], " to ", Cameras[camIdx].name)
            urlopen(Cameras[camIdx].commands[4])
            Cameras[camIdx].state = 0

        disconnect_command = "nmcli con down id " + Cameras[camIdx].name 
        dout = subprocess.Popen(disconnect_command, stdout=subprocess.PIPE, 
                               shell=True, preexec_fn=os.setsid)
        dout.wait()    
        #os.killpg(os.getpgid(dout.pid), signal.SIGTERM)

        return True

        '''
        #while out.returncode == None:
        #    time.sleep(delay)

        #out =  subprocess.check_output(connect_command, stderr=subprocess.STDOUT, shell=True)
        
        #time.sleep(delay)

        out =  subprocess.check_output("iwgetid -r", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        
        if out.replace(" ", "").replace("\n", "") == Cameras[camIdx].name:
            print("Camera Connected")
            return True
        else:
            print(out.replace(" ", "").replace("\n", ""), Cameras[camIdx].name)
            return False

               
        out2 = subprocess.Popen("iwgetid -r", stdout=subprocess.PIPE, shell=True,
                                 preexec_fn=os.setsid)
        os.killpg(os.getpgid(out2.pid), signal.SIGTERM)
        
        while out2.returncode == None:
            time.sleep(delay)
      
        if str(out2.replace(" ", "").replace("\n", "")) == str(Cameras[camIdx].name):
            return True
        else:
            print("Returning False because: ", out2, Cameras[camIdx].name)
            return False
        '''

    except Exception as error :
        print("exception thrown: ", error)
        #time.sleep(delay)
        return False


#Attempts to connect to a camera and returns true if successful.
#waits delay amount of seconds before checking if connection was 
#successful.
def TestCameraConnection_wpa_supplicant(cameraName, delay, supplicant_file_name):
    
    




#Make attempts to switch connections between the two cameras with different delays
#and log the results in a file.
def TestCameraConnectionTime():
    connResults = open("Conn_Results.txt", "w+")
    for delayCounter in range(10, 30):
        connResults.write("\nDelay (in seconds) : " + str(delayCounter * sleep_time) + "\n")
        connResults.flush()
        for count in range(0, 10):
            if connectCamera(0, sleep_time * delayCounter) == True:
                connResults.write("1")
                connResults.flush()
            else:
                connResults.write("0")
                connResults.flush()

            if connectCamera(1, sleep_time * delayCounter) == True:
                connResults.write("1")
                connResults.flush()
            else:
                connResults.write("0")
                connResults.flush()
    connResults.close()

Cameras = []
cameraConfig.readConfig(Cameras)

    
#References :
#1. https://askubuntu.com/questions/16584/how-to-connect-and-disconnect-to-a-network-manually-in-terminal
#2. https://askubuntu.com/questions/117065/how-do-i-find-out-the-name-of-the-ssid-im-connected-to-from-the-command-line
#3. https://docs.python.org/3/library/subprocess.html#subprocess.check_output
#4. https://docs.python.org/3/library/dataclasses.html
#5. https://hackernoon.com/a-brief-tour-of-python-3-7-data-classes-22ee5e046517
#6. https://stackoverflow.com/questions/17178483/how-do-you-send-an-http-get-web-request-in-python
#7. https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
#8. https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
#9. https://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string