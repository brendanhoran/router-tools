#!/usr/local/bin/python3.6

import sys
sys.path.append('/opt/router-tools/python/lib/')
import psutil


# Must set LAN and WAN interfaces
LAN_INT = "em0"
WAN_INT = "ix0"


def interface_stats():
    nic_stats = psutil.net_io_counters(pernic=True)
    lan_stats = nic_stats[LAN_INT]
    wan_stats = nic_stats[WAN_INT]

    nic_state = psutil.net_if_stats()
    lan_state = nic_state[LAN_INT]
    wan_state = nic_state[WAN_INT]

    lan_bytes_rx = lan_stats.bytes_recv
    lan_bytes_tx = lan_stats.bytes_sent
    wan_bytes_rx = wan_stats.bytes_recv
    wan_bytes_tx = wan_stats.bytes_sent

    lan_state_isup = lan_state.isup
    wan_state_isup = wan_state.isup
    return (lan_bytes_rx, 
            lan_bytes_tx, 
            wan_bytes_rx, 
            wan_bytes_tx, 
            lan_state_isup, 
            wan_state_isup)


def cpu_load_stats():
    cpu_load = psutil.cpu_times_percent(interval=1, percpu=False)

    user_load = cpu_load.user
    system_load = cpu_load.system
    irq_load = cpu_load.irq
    return (user_load, system_load, irq_load)


def mem_load_stats():
    mem_status = psutil.virtual_memory()

    mem_used_percent = mem_status.percent
    return mem_used_percent


if __name__ == "__main__":
    (lan_bytes_rx, lan_bytes_tx, wan_bytes_rx, wan_bytes_tx, 
         lan_state_isup, wan_state_isup) = interface_stats()

    user_load, system_load, irq_load = cpu_load_stats()

    mem_used_percent = mem_load_stats()

    print("wan info")
    print("RX: {0:.2f} TX: {1:.2f}".format(
        wan_bytes_rx / 1073741824, wan_bytes_tx / 1073741824))
    print("lan info")
    print("RX: {0:.2f} TX: {1:.2f}".format(
        lan_bytes_rx / 1073741824, lan_bytes_tx / 1073741824))
    print("cpu load")
    print("U: {0:.1f} S: {1:.1f} I: {2:.1f}".format(
        user_load, system_load, irq_load))
    print("mem load : {0:.1f}%".format(mem_used_percent))
    print("LAN is up? : {0}".format(lan_state_isup))
    print("WAN is up? : {0}".format(wan_state_isup))
