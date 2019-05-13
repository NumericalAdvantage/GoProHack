# gp_wifi.py

### It is a collection of functions that can be used to connect to Go Pro's via the access point created on the Go Pro's and sending URL commands via the access point to the Cameras. At one point only one connection can be held and thus only send one GoPro can be sent commands. To send commands to multiple GoPro's, there is a need to switch connections. Please note that it is assumed that you are on a fairly modern distro of Linux.

### Internally gp_wifi.py uses the [wpa_supplicant package](https://linux.die.net/man/8/wpa_supplicant) to manage connections.

### Following points are important to note before using gp_wifi.py:
1. The command `rfkill list` should show that the wifi card is not blocked. If it is, then please use `rfkill unblock`.
2. It is necessary to stop the network manager to make this work smoothly. On Ubuntu this is done using `sudo systemctl stop NetworkManager`. Please find the corresponding command for your distro. 
3. For each camera that you want to connect, you have to create a separate configuration file. This is done using the command: `wpa_passphrase "<GoProSSIDName>" <GoProAccessPointPassword> | sudo tee /etc/<some_file_name>.conf`. This file will be used later in the scripts to connect to the access point. 
4. sample.py is written as an example client file. It does the following: Configures 2 GoPros, sends "locate" command to first goPro, then same command to second goPro. Then it sends "stop locate" command to first and then second goPro. Then it sends "Switch to video mode" command to first goPro and then the second one. Then it sends "start recording" command to the GoPros. And finally it will send the "stop recording" command to the first goPro and then the second goPro.
5. The client files (or sample.py) in this case must be run as root and must use Python 3.x