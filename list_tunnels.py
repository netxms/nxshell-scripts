#!/usr/bin/env nxshell

import csv

with open('tunnels.csv', 'w') as csvfile:
    w = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    w.writerow([
        'IP',
        'Node Name',
        'Hostname',
        'Agent Version',
        'System Name',
        'System Information',
        ])
    for tun in s.agentTunnels:
        w.writerow([
            tun.address.hostAddress,
            s.findObjectById(tun.nodeId).objectName if tun.nodeId != 0 else '<UNBOUND>',
            tun.hostname,
            tun.agentVersion,
            tun.systemName,
            tun.systemInformation,
            ])
