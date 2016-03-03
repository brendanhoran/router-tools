#!/usr/local/bin/python3.4

import sys
sys.path.append('/opt/router-tools/python/lib/')
import router_stats
import os
import serial
import time

bar_led_device = serial.Serial('/dev/ttyU0',
                            baudrate=9600,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=5,
                            xonxoff=0,
                            rtscts=0)

# sleep a little to wait for the arduino to reset
time.sleep(5)


def led_toggle(led_number, state):
  bar_led_data = ("led{0}_{1}".format(led_number, state))
  bar_led_data_encode = str.encode(bar_led_data)
  bar_led_device.write(bar_led_data_encode)
  # sleep a little for the arduino to process
  time.sleep(2)


def wan_online():
  hostname = "horan.hk"
  connection_response = os.system("ping -c 2 " + hostname)
  return connection_response


if __name__ == "__main__":

   (lan_bytes_rx, lan_bytes_tx, wan_bytes_rx, wan_bytes_tx, 
       lan_state_isup, wan_state_isup) = router_stats.interface_stats()

   wan_check_status = wan_online()

   # led1 gets set on by the Arduino at boot time
   # led2 gets auto set always (OS live, script can run)
   # led3 is LAN physical UP
   # led4 is WAN physical UP
   # led5 is we can connect to the internet

   led_toggle(2, 'on')

   if lan_state_isup == True:
     led_toggle(3, 'on')
   else:
     led_toggle(3, 'off')

   if wan_state_isup == True:
     led_toggle(4, 'on')
   else:
     led_toggle(4, 'off')

   if wan_check_status == 0:
     led_toggle(5, 'on')
   else:
     led_toggle(5, 'off')

   bar_led_device.close()
