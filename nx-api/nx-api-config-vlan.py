#!/usr/bin/env python3

import requests
import json
import os
import signal

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Cisco DevNet Sandbox NX - Always On
url = "https://sbx-nxos-mgmt.cisco.com/ins"
switchuser = "admin"
switchpassword = "Admin_1234!"

myheaders = {"content-type": "application/json"}

while True:

    os.system("clear")
    select = input("1. Create VLAN\n2. Delete VLAN\n")
    os.system("clear")

    # If/Else to get input and build commands use in payload
    if select == "1":
        vlan_id = input("Create VLAN - Enter VLAN ID: ")
        vlan_name = input("Create VLAN - Enter VLAN Name: ")
        vlan = "vlan {} ; name {}".format(vlan_id, vlan_name)

    elif select == "2":
        vlan_id = input("Delete VLAN - Enter VLAN ID: ")
        vlan = "no vlan {}".format(vlan_id)

    else:
        continue

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
            "chunk": "0",
            "sid": "sid",
            "input": vlan,
            "output_format": "json",
        }
    }

    # API call to retrieve command defined on the payload
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=myheaders,
        auth=(switchuser, switchpassword),
        verify=False,
    ).json()

    print(json.dumps(response, indent=3))
    input("\n\nPress Enter to continue\n\n")
