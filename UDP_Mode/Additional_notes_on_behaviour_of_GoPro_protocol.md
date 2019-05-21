### Some additional notes on the nature of the protocol:
1. The GoPro sends routine "LCD" messages which are basically a status of the camera wrapped inside a bitmap. As of now I don't know how to decode the bitmap, but should be trivial.
2. The commands issued via UDP are always relayed back to the Smart Remote as a way of acknowledgement.
3. The Smart Remote supports changing settings of the camera depending on the mode you are in. This part of the protocol hasn't been analysed.
4. Sending of UDP commands of course has been tested but receiving hasn't. One major hurdle to this is that since the GoPro's are "fooled" into believing that the Linksys Router is the Smart Remote device, the GoPro's send the responses to the router's IP and not the computer via which we are sending the UDP commands. The GoPro's are not even aware of the existence of the computer actually.  

#### Summary of the behavior of the Smart Remote functionality and some related protocol details.

|Button Press on Smart Remote | UDP message generated                                      | Purpose                   | Description    |
|:----------------------------|------------------------------------------------------------|:-------------------------:|----------------|
|Red Circle                   | '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01'                               | Open Shutter              |This command is used to take a picture in Photo mode, take burst pictures in Burst mode and for Video and time-lapse mode it starts the recording.               |
|Red circle (while a video recording is in progress)| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x00' | Close Shutter             |This command is used to stop the recording for video and time lapse modes. |
|Mode | '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x00' | Switch to Video mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Video mode.|
|Mode | '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x01' | Switch to Photo mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Photo mode.|
|Mode | '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x02' | Switch to Burst mode      |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to Burst mode.|
|Mode | '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x03' | Switch to Time-lapse mode |Notwithstanding the current mode or default mode, issuing this command will switch the GoPro to time-lapse mode.|
|Settings + Mode (while some video recording is in progress)| '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x58\x58\x01\x02' | Make a HiTag |Creates a tag in the video being recorded for the time instant at which the command was issued. Note: This command could not be duplicated in the testing. It is not supported in the Router mode. |
|Settings + Mode (when only one camera is attached to the Smart Remote and no recording is in progress) | Unknown/not analysed | Change various settings for the mode like Linear or Wide angle view, size of image/video, other properties.  | Changes various settings of the camera. |

#### References
1. https://github.com/quine/GoProGTFO
