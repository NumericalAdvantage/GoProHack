# Remote Controlled GoPro's.

## 1. App Mode.
#### This in when the GoPro (HERO6) is set to "App mode" and it creates an access point and we connect to this access point with a computer and we are able to send commands via the browser of the computer to the GoPro.
##### Steps to do this:

1. Switch on the device with power button on the lower right side.
2. Do a "Top to bottom" swipe on the touch screen. Select "Connections". Then select "GoPro App".
3. A screen will appear on the touchscreen with data with which
we can connect to the camera from the PC - i.e. the name of the access point and password. This means the access point (AP) is created.
4. Next we want to connect the computer to the GoPro access point. To do this, enter the  password on the computer and you will be connected to the AP.
5. Test your connection by issuing the following command via the browser to turn GoPro off - `http://10.5.5.9/gp/gpControl/command/system/sleep` in the browser's address bar.

[This is a script](https://gitlab.hrz.tu-chemnitz.de/righ--tu-chemnitz.de/righ-gopro-wifi-remotecontrol_poc/blob/master/GP_Record.py) that implements the above method and can be expanded with new information from [this project on github](https://github.com/KonradIT/goprowifihack) which was also the central source of this part of the remote control.

## 2.  Smart remote  
#### This is when we use a router to create a fake access point to which we connect our GoPro(s) (GoPro model used is HERO6) and the computer which we want to use to send commands to the GoPro(s). The GoPro is made to believe it is connecting to a GoPro Smart Remote however what is actually happening is that the GoPro is connecting to the access point created by the router to which our "remote control computer" is also connected. We send commands to this GoPro by sending UDP messages to it via the computer. The router used was a LINKSYS Wireless-G broadband Router. Model Number: WRT54GL v1.1. Firmware: DD-WRT v24-sp2 (08/07/10)

##### Steps to configure the router:
1. Power up and hold the rest button for 30 secs.
2. Start the web interface via 192.168.0.1
3. On Setup tab, under Basic Setup, mark the Connection Type setting in WAN Connection Type to Disabled. Set the local IP address to 10.71.79.1
4. In the Setup tab, under MAC Address Clone, enter the following address under Clone Wireless MAC: D8:96:85:00:00:00.
5. Under the Wireless tab, under basic Settings, select AP for Wireless mode. Set Wireless Network Mode to Mixed. Set the Wireless Network Name (SSID) to HERO-RC-000000.
6. Under security tab, Set SPI Firewall to Disable.
7. Restart router. Restart computer. Use the IP address in point 4 above to access the web interface.
8. On you computer you should now be able to see an Access Point called "HERO-RC-000000". Connect to it.
9. On the Go Pro, select Connections by top->down swipe and select Reset Connections. Then do Connect New Device -> Smart Remote.
10. You should see an entry for the Go Pro on the web interface's Status -> LAN page. You should also see a confirmation message on the Go Pro.

##### Actually sending commands from the computer to the GoPro(s):
1. A router is configured as per the 10 steps above and is switched on.
2. A GoPro is started, and it automatically latches on to the access point created by the router above when we try Connections->Connect New Device->Smart Remote. (Note that you may need to do Connections->Reset Connections first!).
3. A computer is also connected to the access point created by the router.
4. The mode on the GoPro is "Video".

##### If the above steps are all done, then the following command starts a video recording when executed in a bash shell on the computer that was used to join the access point from the router:
`echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xfe\x53\x48\x01' >/dev/udp/<IP of the connected GoPro>/8484`

##### And the following command stops the recording (also executed in the bash shell of the same computer):
`echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x92\x53\x48\x00' >/dev/udp/<IP of the connected GoPro>/8484`

#### Note:
1. The IP address used above is attained from the router's settings page. Status->LAN-> would have it.

2. The mode is not yet controlled from the computer and the goPro must be already in Video Mode before the commands are issued. If mode is changed physically on the GoPro, it doesn't matter as long as the mode is switched back to Video and the commands are fired from the laptop. Also, sometimes I have observed that I will set the GoPro to Video mode, but after the GoPro connects to the fake access point, its mode is automatically switched to Photo. No idea why this happens, but a simple solution is to manually switch the GoPro back to Video mode.

3. The above commands also seem to be working with other modes. Even though I haven't tested those scenarios fully.

## 2. b) How was this done?
1. It was known from [here](http://azzure.org/gopro/index.htm) and [here](https://goprohero.readthedocs.io/en/latest/Wifi%20Research/) that the way Smart Remote feature works is that the GoPro automatically connects to an access point created with the beginning part of the SSID as "HERO-RC-". So first step was to use a router to do just this - create an access point.
2. Next step was to understand the way in which the Smart Remote device works with the GoPro, i.e., what are the commands it sends? One crucial thing we needed for this was to discover the name of the hidden WiFi network that the Smart Remote creates. [This resource](https://kalitutorial.com/node/2) was used to do this.
3. It was already known that the Smart Remote sends commands to the GoPro via UDP. So to actually see what commands are being sent to the GoPro, a set up was created as described below:
   1. Switch on the Smart Remote and set it to "pairing".
   2. Connect the computer to the Smart Remote's access point.
   3. Start a monitoring session for the wireless interface on the computer using Wireshark.
   4. Send various commands to the GoPro from the Smart Remote and observe the network traffic.
4. From the above set up we are able to see many UDP messages that were getting sent to the GoPro. Next step was to duplicate the same thing (UDP messages) from the computer and see if we can get the same behaviour like starting and stopping recordings. The following set up was used for this purpose:
  1. Start the router with the configurations as described previously. This basically enables the router to masquerade as a Smart Remote.
  2. Start the GoPro and wait until it connects to this fake access point when we attempt to configure it in Smart Remote mode.
  3. Connect to the same "fake access point" from the computer as well.
  4. Now send various UDP commands to the connected GoPro from the bash shell of the computer and see what happens on the GoPro.
5. After a while a few commands were discovered by the hit and trial method described above.

## 3. Connecting two Go Pro's to a computer.
#### The aim here is to get more than one Go Pro connected together to the wireless access point (as described in point 2) such that we are able to send independent commands to the Go Pro's.

The configuration for the router needs to be made as discussed in point 2. After that, just switching on multiple goPro's and trying to pair them using Smart Remote leads to them being getting latched on to the router's access point. To send commands to the new goPro, its IP address needs to be known from the router's settings page as per steps described in the previous section.

## 4. List of commands.

1. Start recording -   
`echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xfe\x53\x48\x01' >/dev/udp/<IP of the connected GoPro>/8484`
2. Stop recording -    
`echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x92\x53\x48\x00' >/dev/udp/<IP of the connected GoPro>/8484`
