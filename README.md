*** WORK IN PROGRESS ***

# Overview
#### Why do this?  
I got sick of trying to find a decent vendor device to support 1gbit+ WAN connections in Hong Kong.     
So that means building my own router, thus I wanted some nice LED's / LCD to provide quick feedback.
#### What does it support
Currently OpenBSD (5.8) However aside from the LCDproc (LCDd) binary the python code should work on any device.
#### what will the tools give me?
1. A status LCD that shows traffic,load and uptime information
2. A barLED that shows connectivity states
3. A simple way to update a Hurricane Electric IPv6 tunnle (OpenBSD only)

# Hardware   
The project has four main hardware parts  

1. The physical graplical LCD (KS0108)
2. Till Harbaum's GLCD2USB board
3. Arduino nano (ATmega328)
4. Five segment bar LED
Miscilanious parts : usb cable, usb hub, plastic project box

# Software
The projects make heavy use of    

1. Python
2. Pythin libarys used (lcdproc, psutil, pyseril + my own libarys) 
2. shell (ksh)
3. LCDproc (OpenBSD, needs package libusb-compat)

