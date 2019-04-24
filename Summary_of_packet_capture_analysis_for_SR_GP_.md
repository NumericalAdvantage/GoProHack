## Packet Capture analysis -
#### (Each of the following points generated a pcap file for analysis which is stored on my drive)
1. **Just the SR turned on and then pairing turned on on the SR** - No UDP messages (obviously)
2. **One gp connects** - To and fro of some set of UDP messages. Could not exactly figure out any protocol. Observed some things like some numbers getting incremented in hex. Not sure if converting to some other number formate would help. Definitely would try later with more data and converting the payload to decimal. ASCII conversion shows some letters like w t, p w, s t; but no idea right now what they mean.   
3. **One gp connects and I take a picture** - Somethings were as per expectation, for example the start of the sequence of UDP message exchange, but then things got a bit weird. Encountered at least 2 types of messages which I haven't seen before. One of them was 600 bytes+ in length. Another one where the data seems to be very different from the previous runs.
4. **One gp connects and I make a video (GP was originally in video mode)** - some "' l c" messages I can see whose purpose I cannot understand. Noticed that when a prior connection is not terminated and we restart the SR, the count (sequence) from previous time is used. That number is saved in the GP. Weird thing is that I could not see the UDP message which I know activates the shutter. So not sure if  
5. **One gp connects and I take a photo (GP was originally in video mode)** - Did not observe anything very peculiar in this run. Might need to look again.
6. **One gp connects and I change the mode once** - Only one message stood out. I have marked it and will try to use it to switch modes using the router later. However, the data isn't exactly legible and if it is dependent on some previously sent data (like the counter/sequence) then i would be helpless.  
7. **One gp connects and I change the mode twice** - Was able to pinpoint the messages which were causing the switch. Noticed that there is a subtle change in the message but not sure if that has got to do with the sequencing and other parts of the protocol or the mode switch itself. Note that I still don't know what the message actually "means". This is just rote pattern matching.
8. **Two gp connect** - Found some issues with SR and GP's. Like one of the GP's didn't connect but the SR said it had two connections! Could not put the SR back into the pairing mode once one GP connected and I wanted to connect another one. Another time the SR said it had only one camera but was actually controlling two. Only after a while did it correct itself. Also, if we had prior connections, then the SR when switched on, automatically connects to the GP's. The channel was switched all of a sudden. Not sure what triggered it or why. But this is the first time I am observing it. And then next time it switched it back again. But the strangest part was that No UDP data was generated.
9. Two gp connect (both have default mode photo) and I take a picture.
10. Two gp connect (both have default mode video) and I switch mode and take a picture.
11. Two gp connect (one has default mode video and the other has default mode picture) and I switch modes to video and take a video.
12. Two gp connect (one has default mode video and the other has default mode picture) and I switch modes to picture and take a photo.
13. Two gp connect (one has video mode, other has burst mode) and I switch modes to picture and take a photo.


###### In summary, the protocol is much more complex that I thought. There is constant back and forth of UDP messages between the SR and the GP and the meaning of the messages is not clear. Even running the connection between one GP and SR for less than 15 seconds generates around 120+ UDP messages.
###### I actually have a suspicion that there is more than one way to do things like taking a picture or start/stop of video.
###### The "big messages" that I observed in some runs were not present in others. I think they might be carrying data about the camera settings, etc. They don't make any sense when converted to ASCII, which means they are using some sort of look up tables or messaging codes type approach or something similar.
###### I think it would help (but only a little) if I had a "live" way of viewing the packet capture dump file.
###### Have identified the messages which cause the mode switch. Will be testing them through the router soon.
###### The SR fucntionality is not perfect when it comes to handling more than one GP. There are definitely bugs. I doubt they have many users for multiple GP with a single SR configuration. Because I could easily reproduce a bug or two.
###### I didn't finish 9 thru 13, but did just one run where I basically tried everything with multiple GP's like switching modes and activating the shutter. I don't think the mechanism to switch modes is same as in the case of a single GP. And it was a bit more complicated as expected. A lot of analysis is needed in my view.
###### Not sure if moving forward with 9-13 is better or trying my hunches on the router is better/faster.

## gitlab check-in

1. check in the iwconfig script.
2. check in the tables and scripts for sending UDP commands.

## gitlab issue TC9
1. perform analysis.
2. formulate results in a table
3. Create scripts.
