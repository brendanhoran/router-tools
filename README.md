# Overview
#### Why do this?  
I got sick of trying to find a decent vendor device to support 1gbit+ WAN connections in Hong Kong.     
So that means building my own router, thus I wanted some nice LED's / LCD to provide quick feedback.

#### What does it support
Currently OpenBSD (5.9) However aside from the LCDproc (LCDd) binary the python code should work on any device.
Unless otherwise noted that the script is just for OpenBSD.

#### what will the tools give me?
1. A status LCD that shows traffic,load and uptime information
2. A barLED that shows connectivity states (Device power,System up, LAN up, WAN up, Connectivity test)
3. A simple way to update a Hurricane Electric IPv6 tunnle (OpenBSD only)
4. A simple script to check for OpenBSD errta patches

## Hardware   
The project has four main hardware parts  

1. The physical graplical LCD (KS0108)
2. [Till Harbaum's GLCD2USB board](https://github.com/harbaum/GLCD2USB)
3. Arduino nano (ATmega328)
4. Five segment bar LED
Miscilanious parts :
* usb cable 
* usb hub 
* plastic project box

## Software
The projects make heavy use of    
1. Python
2. Pythin libarys used (lcdproc, psutil, pyseril + my own libarys) 
2. shell (ksh)
3. LCDproc (OpenBSD, needs package libusb-compat)

