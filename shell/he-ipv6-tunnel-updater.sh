#!/bin/ksh
# Description :
#   A simple script to update the local(gif) tunnel with the new WAN IP
#   and also update HE(tunnelbroker) with the new end point IP
#   This also depends on a line in /etc/rc.local :
#   "/sbin/ifconfig ix0 | grep inet | cut -c 7-21 | xargs > /tmp/.wan-ip"


### Variables that must be set ###
###
# HE tunnel endpoint
HE_tunnel_end=""

# HE username
HE_user_name=""

# HE update key
HE_update_key=""

# HE tunnel ID
HE_tunnel_id=""

# Local WAN interface
wan_interface=""

# Local interface for tunnel
tunnel_interface=""

###
### End variables ###


# WAN IP on system boot
wan_ip=`cat /tmp/.wan-ip`

# Current WAN IP from adaptor
ifconfig $wan_interface | grep inet | cut -c 7-21 | xargs > /tmp/ip
current_wan_ip=`cat /tmp/ip`

# Check to see if the WAN IP has changed
ip_diff_check=`diff -s /tmp/.wan-ip /tmp/ip`
returncode_ip_diff_check=`echo $?`

# If changed, then update the tunnel and update HE, if no change exit and log msg to syslog
if [ $returncode_ip_diff_check != 0 ]; then
  sed -i "1 s/^.*$/tunnel $current_wan_ip $HE_tunnel_end/g" /etc/hostname.$tunnel_interface
  /bin/sh /etc/netstart $tunnel_interface
  curl -s "https://$HE_user_name:$HE_update_key@ipv4.tunnelbroker.net/nic/update?hostname=$HE_tunnel_id"
  logger "Updated HE tunnel with new local IP $current_wan_ip"
  mv /tmp/ip /tmp/.wan-ip
else
  logger "No update needed for HE IPV6 tunnel"
  exit 0
fi
