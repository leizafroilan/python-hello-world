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

while True:

    # Accepts show commands to be sent to NX
    show_cmd = input("Enter show commands here: ")

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "sid",
            "input": show_cmd,
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

    print(json.dumps(response, indent=3))
