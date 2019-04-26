## List of verified commands for the Smart-Remote GoPro hack.

| UDP message                                                | Purpose                   |
| -----------------------------------------------------------|:-------------------------:|
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01' | Open Shutter              |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x00' | Close Shutter             |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x00' | Switch to Video mode      |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x01' | Switch to Photo mode      |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x02' | Switch to Burst mode      |
| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x03' | Switch to Time-lapse mode |


###### Note that the fourth last byte in the UDP message must always be alternated between /x00 and /x01 between successive commands.
###### For non video modes like Picture and Burst, there is no need to issue "Close Shutter" command.
###### On Linux using the bash shell, the UDP message can be sent using `echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01' >/dev/udp/<IP_address_of_GP>/8484`
