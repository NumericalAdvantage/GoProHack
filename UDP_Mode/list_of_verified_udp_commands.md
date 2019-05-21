## List of verified commands for the Smart-Remote GoPro hack.

| UDP message                                                | Purpose                   | Description    |
| -----------------------------------------------------------|:-------------------------:|----------------|
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01' | Open Shutter              |This command is used to take a picture in Photo mode, take burst pictures in Burst mode and for Video and time-lapse mode it starts the recording.               |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x00' | Close Shutter             |This command is used to stop the recording for video and time lapse modes. |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x00' | Switch to Video mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Video mode.|
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x01' | Switch to Photo mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Photo mode.|
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x02' | Switch to Burst mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Burst mode.|
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x03' | Switch to Time-lapse mode |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to time-lapse mode.|


###### Note that the fourth last byte in the UDP message must always be alternated between /x00 and /x01 between successive commands.
###### On Linux using the bash shell, the UDP message can be sent using `echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01' >/dev/udp/<IP_address_of_GP>/8484`
