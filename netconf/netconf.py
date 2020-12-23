#!/usr/bin/env python3


from ncclient import manager
import xmltodict
import json
import os

lines = []

choice = input(f"1. get\n2. get_config\n3. edit_config\nSelect: ")

os.system("clear")

print(("Enter Filter/Config Here\n"))

# Builds config/filter and stores on list
while True:
    raw = input()

    if "</filter>" in raw or "</config>" in raw:
        lines.append(raw)
        break
    else:
        lines.append(raw)

# Saves filter/config as str
netconf_filter = "\n".join(lines)

# Connects to csv1000v Cisco Always-On Sandbox using netconf
with manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port="10000",
    username="developer",
    password="C1sco12345",
    hostkey_verify=False,
    ) as m:

    if choice == "1":
        # Gets running and state
        m_reply = m.get(netconf_filter)
    elif choice == "2":
        # Gets running
        m_reply = m.get_config("running", netconf_filter)
    elif choice == "3":
        # Edits running
        m_reply = m.edit_config(target="running", config=netconf_filter)
    else:
        pass

m_reply_dict = xmltodict.parse(m_reply.xml)

print(json.dumps(m_reply_dict, indent=1))
