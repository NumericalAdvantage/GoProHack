#!/bin/bash

echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x01' >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5


echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x43\x4d\x00'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x00'	 >/dev/udp/10.71.79.133/8484
sleep 5


echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x02' >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5

echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x43\x4d\x03'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x48\x01'	 >/dev/udp/10.71.79.133/8484
sleep 5
echo -n -e '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x53\x48\x00'	 >/dev/udp/10.71.79.133/8484