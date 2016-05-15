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
3. A simple way to update a Hurricane Electric IPv6 tunnel (OpenBSD only)
4. A simple script to check for OpenBSD errata patches

## Hardware   
The project has four main hardware parts  

1. The physical graplical LCD (KS0108)
2. [Till Harbaum's GLCD2USB board](https://github.com/harbaum/GLCD2USB)
3. Arduino nano (ATmega328)
4. Five segment bar LED
Miscellaneous parts :
* usb cable 
* usb hub 
* plastic project box

## Software
The projects make heavy use of 

1. Python
2. Pythin libarys used (lcdproc, psutil, pyseril + my own libarys) 
2. shell (ksh)
3. LCDproc (OpenBSD, needs package libusb-compat)

## How to use

### LCD
Build the LCD and USB interface as per guide on Till Harbaum's page.
OpenBSD needs the "libpthread.so" share library pre loaded for LCDproc to work.
I wrote a simple [wrapper script](https://github.com/brendanhoran/router-tools/blob/master/lcdproc/start-lcd-server.sh) to take care of that.
I then have the following in "/etc/rc.local"
"cd /opt/router-tools/lcdproc/ && ./start-lcd-server.sh"

To start the LCDproc client I have this in "/etc/rc.local"
"/opt/router-tools/python/scripts/lcd-client.py &"

### Bar LED
This assumes you have flashed the Arduino code to your Ardunio. Bar led's in the current Arduino code are connected to digital pins 2 to 5.
I then have the following in "/etc/rc.local"
"/opt/router-tools/python/scripts/bar-led-control.py &"

I also have a cron job set to re run the “bar-led-crontrol.py” script every 10mins

### IPv6 Tunnel updater
*OpenBSD only*

This script depends on a line in "/etc/rc.local" to save the current WAN IP to a file
"/sbin/ifconfig ix0 | grep inet | cut -c 7-21 | xargs > /tmp/.wan-ip"
Where ix0 is my WAN interface. I do not need to log into my ISP, DHCP only.
If that is not the case for you this would need to change to run after your WAN is UP.

Then via cron I run "/opt/router-tools/shell/tunnel-updater.sh" evry 15mins to check if the WAN IP has changed.
If the WAN IP has changed , update the IPv6 tunnel end point and update HE with the new WAN IP.
Small note, this script is not very safe for a multi user machine. However since there is no one but myself logged in/using my router I don't care. Susgestions welcome

### Errata Checker
*OpenBSD only*

Once a week cron runs "/opt/router-tools/shell/errata-checker.sh" to check for new OpenBSD errata.
This script is heavy depend on a set directory structure. 
I have the following :
/root/patches/$VER_NUM/$PATCH_NUM
I save the sig file to "/root/patches/$VER_NUM/". For example the "001_sshd.patch.sig" patch for OpenBSD 5.9 would be saved as:
"/root/patches/59/001_sshd.patch.sig"

The script checks "/root/patches/$VER_NUM/" and compares that with the list of patches on the Errata page.
The script will not apply or even download patches. I do that by hand.
