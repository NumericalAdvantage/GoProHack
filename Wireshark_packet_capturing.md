# Monitoring mode vs Promiscuous mode packet capturing in Wireshark.

## Promiscuous mode

#### Definition

Sniffing (capturing) the packets of a wireless network after connecting to an access point.

#### Intuitive explanation
Think of it like joining a group of people in a conversation, but at the same time being able to hear when someone says "Hey, Mike, I have a new laptop". Even though you're not Mike, and that sentence was intended to be heard by Mike, but you're still able to hear it just because you are part of the conversation. You have access to the conversation and you are abusing that privilege to listen to things that are not actually concerning you. Other people in the conversation don't expect you to listen to things which don't concern you, but they know that if you want to do so, you can, because in the end, you are part of the conversation.

#### Technical explanation
Promiscuous mode is possible because the wireless-enabled devices send the data in the air but only "mark" them to be processed by the intended receiver. They cannot send the packets and make sure they only reach a specific device, unlike with switched LANs.

The driver still outputs standard ethernet frames belonging to the one wireless network you are currently associated to (identified by the BSSID).

Promiscuous mode allows you to view all wireless packets on a network to which you have associated. It basically tells the card to process all frames, (i.e. remove 802.11 frame headers) including those not destined for it.

Associated means you must have some means of authenticating yourself with an access point. In promiscuous mode, you will not see packets until you have associated. Not all wireless drivers support promiscuous mode.

Even in promiscuous mode, an 802.11 adapter will only supply packets to the host of the SSID the adapter has joined. Although it can receive, at the radio level, packets on other SSID's, it will not forward them to the host.

## Monitor mode

#### Definition
Sniffing the packets in the air without connecting (associating) with any access point.

#### Intuitive explanation
Think of it like listening to people's conversations while you walk down the street. The people talking are strangers. You don't know them and they don't know you. Moreover, they have no idea that you are actually eavesdropping on their conversations.

#### Technical explanation
In monitor mode the SSID filter is disabled and all packets of all SSID's from the currently selected channel are captured. In "monitor mode", you capture packets from all the networks operating on a chosen channel, and the driver does not output plain ethernet, but needs to output more headers (there are 3 addresses in a 802.11 header, instead of just 2 addresses in the 802.3 ethernet headers). Only special wireless monitoring software is able to process packets in the format dumped by the driver in monitor mode.

So monitor mode is advantageous if you want to really see what's going on, while promiscuous mode is there for compatibility with standard ethernet network sniffing tools that can't handle the extended 802.11 frame format. If the tool you want to use supports monitor mode, use it. Use promiscuous mode only as backup.

Monitor mode has the advantage of not having to be associated with the AP. This makes it possible to be completely invisible, and to sniff packets on a network you don't have the password for. In promiscuous mode you have to associate with the AP, so you are sending out packets. Monitor mode can be completely passive.

In addition, monitor mode allows you to find hidden SSIDs. SSIDs aren't broadcast by the AP, but they are broadcast by the client. Monitor mode tells the card to pass along the frames intact (with 802.11 headers) and not present Ethernet frames to the host.

So in order to capture all traffic that the adapter can receive, the adapter must be put into "monitor mode", sometimes called "rfmon mode". In this mode, the driver will not make the adapter a member of any service set, so it won't support sending any traffic and will only supply received packets to a packet capture mechanism, not to the networking stack. This means that the machine will not be able to use that adapter for network traffic; if it doesn't have any other network adapters, it will not be able to.

Steps in [7] need to be followed before we are able to capture packets in monitor mode. Basically, the device needs to be put in monitoring mode (by following the steps in [7]) and then packet capture needs to be started in Wireshark.

### References:
1. https://wiki.wireshark.org/CaptureSetup/WLAN#Linux
2. https://medium.com/@debookee/promiscuous-vs-monitoring-mode-d603601f5fa
3. https://security.stackexchange.com/questions/36997/what-is-the-difference-between-promiscuous-and-monitor-mode-in-wireless-networks
4. https://security.stackexchange.com/questions/80500/promiscuous-vs-monitor-mode-in-802-11?noredirect=1&lq=1
5. http://lazysolutions.blogspot.com/2008/10/difference-promiscuous-vs-monitor-mode.html
6. http://www.wireless-nets.com/resources/tutorials/sniff_packets_wireshark.html
7. http://www.aircrack-ng.org/doku.php?id=airmon-ng
