#!/bin/bash
#Please note that you have to change the IP address before you run the script to the IP address that is
#assigned to the GoPro you are working with by the router which you are using to create the fake Smart Remote Access Point.

#Switch to Photo and take a picture.
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x01' >/dev/udp/10.71.79.133/8484
sleep 5 #give the GP a moment to make the switch
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5 #small pause before we make the next switch

#Switch to Video and take a 5 second video.
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x00'	 >/dev/udp/10.71.79.133/8484
sleep 5 #give the GP a moment to make the switch
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x00'	 >/dev/udp/10.71.79.133/8484
sleep 5 #small pause before we make the next switch

#Switch to Burst and take a burst.
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x02' >/dev/udp/10.71.79.133/8484
sleep 5 #give the GP a moment to make the switch
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5 #small pause before we make the next switch

#Switch to Time-lapse and take a time lapse.
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x03'	 >/dev/udp/10.71.79.133/8484
sleep 5 #give the GP a moment to make the switch
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x00'	 >/dev/udp/10.71.79.133/8484
