# gp_wifi.py

### It is a collection of functions that can be used to connect to Go Pro's via the access point created on the Go Pro's and sending URL commands via the access point to the Cameras. At one point only one connection can be held, and thus only one GoPro can be sent commands. To send commands to multiple GoPro's, there is a need to switch connections. Please note that it is assumed that you are on a fairly modern distro of Linux.

### Internally gp_wifi.py uses the [wpa_supplicant package](https://linux.die.net/man/8/wpa_supplicant) to manage connections.

### Following points are important to note before using gp_wifi.py:
1. The command `rfkill list` should show that the wifi card is not blocked. If it is, then please use `rfkill unblock`.
2. It is necessary to stop the network manager to make this work smoothly. On Ubuntu this is done using `sudo systemctl stop NetworkManager`. Please find the corresponding command for your distro. 
3. For each camera that you want to connect, you have to create a separate configuration file. This is done using the command: `wpa_passphrase "<GoProSSIDName>" <GoProAccessPointPassword> | sudo tee /etc/<some_file_name>.conf`. This file will be used later in the scripts to connect to the access point. 
4. sample.py is written as an example client file. It does the following: Configures 2 GoPros, sends "locate" command to first goPro, then same command to second goPro. Then it sends "stop locate" command to first and then second goPro. Then it sends "Switch to video mode" command to first goPro and then the second one. Then it sends "start recording" command to the GoPros. And finally it will send the "stop recording" command to the first goPro and then the second goPro.
5. The client files (sample.py in this case) must be run as root and must use Python 3.x
6. If the "Reset Connections" function is not used on the GoPro, the GoPro does not change the password for the access point.
7. One conclusion: there are going to be some changes when we use different computers to run the scripts, atleast on my system (Lenovo ThinkPad T470 running Ubuntu 16.04 LTS, Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78),	Subsystem: Intel Corporation Dual Band Wireless-AC 8265) I see that the only noticeable "lag" is when we send a URL command to the GoPro and are waiting for the GoPro to respond. This sadly, is out of our hands. We are prisoners of the GoPro's whims. The network switch is _near_ instantaneous. 
8. Debugging tip: Use the `--verbose`, `--trace` flags by modifying the `sendCommand()` function in gp_wifi.py to see how things are working, what is taking more/less time. 
9. One pet-peeve of wpa_supplicant: It is necessary to kill `wpa_supplicant` process before you can switch connection to another SSID/access_point.
10. Further improvements: The functions from gp_wifi.py should be put into a class. This class object should be used to run all the functions. This would help to hide certain things from the user like calling the `initialization()` function, maintaining connections when multiple commands are to be sent via `cURL`, automatically figure out if a connection is being attempted for the first time, and if yes, fire the dhclient command among other things. I am not doing it right now, because a lot of this class design would depend on "how the experiment" is to be run. Questions like "would we have all the commands to be run and their corresponding camera names before hand?" need to be answered. cURL works fine, but may be we also test how netcat, wget, some other alternative behave to send commands. Same with wpa_supplicant. We can also have a function in the class which reads the config file and automatically performs the task of `wpa_passphrase`. 

## References
1. https://wiki.archlinux.org/index.php/WPA_supplicant
2. https://linuxcommando.blogspot.com/2013/10/how-to-connect-to-wpawpa2-wifi-network.html
3. https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant
4. http://linux.icydog.net/wpa.php
5. https://askubuntu.com/questions/138472/how-do-i-connect-to-a-wpa-wifi-network-using-the-command-line
6. https://linuxize.com/post/curl-command-examples/
7. https://ec.haxx.se/cmdline-urls.html
