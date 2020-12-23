#!/usr/bin/env python3

import requests
import json
import signal

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Cisco DevNet Sandbox NX - Always On
url = "https://sbx-nxos-mgmt.cisco.com/ins"
switchuser = "admin"
switchpassword = "Admin_1234!"

myheaders = {"content-type": "application/json"}

# Show ip interface brief to be sent as payload
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "sid",
        "input": "show ip int brief",
        "output_format": "json",
    }
}

# API call to retrieve show command defined on the payload
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

# Parses response to get interface details
interfaces = response["ins_api"]["outputs"]["output"]["body"]["TABLE_intf"][
    "ROW_intf"
]

print("Getting interface for sbx-nxos-mgmt.cisco.com")

for interface in interfaces:
    print(
        "VRF Name: {}\nInterface Name: {}\nLink State: {}\nAdmin State: {}\nPrefix: {}".format(
            interface["vrf-name-out"],
            interface["intf-name"],
            interface["link-state"],
            interface["admin-state"],
            interface["prefix"],
        )
    )
