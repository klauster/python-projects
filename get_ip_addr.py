#!/usr/bin/python

# Get host IPs from hostname
# looks for "servers.txt" as input file
# writes to server name and IP addresses to "ip_addr.txt"

import time
import socket

srvr_file = open('servers.txt', "r")
ip_file = open('ip_addr.txt', "w")

lines = srvr_file.readlines()

for n in lines:
    hostname = n.strip()
    try:
        ipaddr = socket.gethostbyname(hostname)
        host_string = hostname + "," + ipaddr + "\n"
        ip_file.write(host_string)
    except socket.error:
        host_string = hostname + ", IP not found" + "\n"
        ip_file.write(host_string)

srvr_file.close
ip_file.close