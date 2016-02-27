#!/bin/ksh
# Pre load of lib is needed for OpenBSD

LD_PRELOAD=/usr/lib/libpthread.so ./LCDd -c LCDd.conf
