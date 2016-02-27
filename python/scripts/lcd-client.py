#!/usr/local/bin/python3.4

import os
import sys
sys.path.append('/opt/router-tools/python/lib/')

import time
import datetime
import threading
import router_stats

# LCD layout notes
# y= means LCD ROW
# x= means LCD column

from lcdproc.server import Server


def write_to_lcd():
    lcd = Server("localhost", debug=False)
    lcd.start_session()

    screen1 = lcd.add_screen("screen1")
    screen1.set_heartbeat("off")

    system_uptime = os.popen('uptime | cut -c 13-17').read()
    system_uptime = system_uptime.rstrip()

    (lan_bytes_rx, lan_bytes_tx, wan_bytes_rx, wan_bytes_tx,
        lan_state_isup, wan_state_isup) = router_stats.interface_stats()
    user_load, system_load, irq_load = router_stats.cpu_load_stats()
    mem_used_percent = router_stats.mem_load_stats()

    string_widget = screen1.add_string_widget(
        "wan_info_title", text="WAN data (gb):", x=1, y=1)

    string_widget = screen1.add_string_widget("wan_info_data",
        text="RX:{0:.2f} || TX:{1:.2f}".format(
                                               wan_bytes_rx / 1073741824,
                                               wan_bytes_tx / 1073741824),
                                               x=1, y=2)

    string_widget = screen1.add_string_widget(
        "lan_info_title", text="LAN data (gb):", x=1, y=3)
    string_widget = screen1.add_string_widget("lan_info_data",
        text="RX:{0:.2f} || TX:{1:.2f}".format(
                                               lan_bytes_rx / 1073741824,
                                               lan_bytes_tx / 1073741824),
                                               x=1, y=4)

    string_widget = screen1.add_string_widget(
        "cpu_info_title", text="CPU load:", x=1, y=5)
    string_widget = screen1.add_string_widget(
        "cpu_info_data", text="U: {0:.0f}% S: {1:.0f}% I: {2:.0f}%".format(
        user_load, system_load, irq_load), x=1, y=6)

    string_widget = screen1.add_string_widget(
        "mem_info", text="MEM load: {0:.1f}% used".format(
        mem_used_percent), x=1, y=7)

    string_widget = screen1.add_string_widget(
        "sys_uptime", text="Uptime: {0}".format(system_uptime), x=1, y=8)


while True:
    write_to_lcd()
    time.sleep(10)

if __name__ == "__main__":
    main()
