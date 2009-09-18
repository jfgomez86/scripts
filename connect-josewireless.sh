#!/bin/bash
ifconfig wlan0 up
iwconfig wlan0 essid josewireless
iwconfig wlan0 key s:lonecatwifi
dhclient wlan0
