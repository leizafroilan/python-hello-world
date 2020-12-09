#!/usr/bin/env python3

import requests
import yaml
import os
import signal
from getters import (
                main_getter,
                device_getter,
                type_getter,
                vendor_getter,
                role_getter,
                interface_getter,
                site_getter
                    )
from headers import form_headers


headers = form_headers()
base_url = "http://192.168.10.235/api"

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)


# Add site to Netbox - 192.168.10.235
def add_site(name, slug):

    url = base_url + "/dcim/sites/"
    print(url)
    payload = {
            "name": name,
            "slug": slug
                }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    print(f"\nStatus code: {response.status_code}")
    input(response.text)


# Add role to Netbox - 192.168.10.235
def add_role(name, slug, desc):

    url = base_url + "/dcim/device-roles/"

    payload = {
        "name": name,
        "slug": slug,
        "description": desc
            }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    print(f"\nStatus code: {response.status_code}")
    input(response.text)


# Add vendor to Netbox - 192.168.10.235
def add_vendor(vendor, slug):

    url = base_url + "/dcim/manufacturers/"

    payload = {
        "name": vendor,
        "slug": slug,
        "description": vendor
            }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    print(f"\nStatus code: {response.status_code}")
    input(response.text)


# Add vendor to Netbox - 192.168.10.235
def add_device_type(manufacturer, model, slug):

    url = base_url + "/dcim/device-types/"

    payload = {
            "manufacturer": manufacturer,
            "model": model,
            "slug": slug,
            }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    print(f"\nStatus code: {response.status_code}")
    input(response.text)


# Add IP to Netbox - 192.168.10.235
def add_ip(ip, device_id, name, interface_id):

    url = base_url + "/ipam/ip-addresses/"

    payload = {
        "address": ip + "/24",
        "assigned_object_type": "dcim.interface",
        "assigned_object_id": interface_id,
        "assigned_object": {
            "id": interface_id,
            "device": {
                "id": device_id,
                "name": name,
                "display_name": name,
                "interface": "FastE"
                },
            "name": "FastE"
                    }
        }

    response = requests.post(url, headers=headers, json=payload, verify=False)
    print(f"Status code: {response.status_code}")
    input(response.text)


# Add interface to Netbox - 192.168.10.235
def add_interface(device):

    url = base_url + "/dcim/interfaces/"

    payload = {
            "device": device,
            "name": "FastE",
            "type": "virtual",
            "enabled": True
    }

    response = requests.post(url, headers=headers, json=payload, verify=False)
    print(f"\nStatus code: {response.status_code}")
    print(response.text)


# Add device to Netbox - 192.168.10.235
def add_device(site, name, type, role):

    url = base_url + "/dcim/devices/"

    payload = {
            "name": name,
            "device_type": type,
            "device_role": role,
            "serial": "",
            "asset_tag": name,
            "site": site,
            "status": "active",
            "comments": name,
            "local_context_data": ""
            }

    response = requests.post(url, headers=headers, json=payload, verify=False)

    os.system("clear")
    print(f"Status code: {response.status_code}")
    print(response.text)

    # Checks if device already exist, if not exist, executes code below
    # Other status code other than 201 means device is not added
    if response.status_code == 201:

        # Get request to query all devices and stores to variable devices
        devices = device_getter()

        # Loops to all devices, adds interface and IP address to newly added
        # device
        for device in devices:

            if device["name"] == name:
                device_id = device["id"]
                add_interface(device_id)

                interfaces = interface_getter()

                for interface in interfaces:
                    if interface["device"]["name"] == k:
                        add_ip(v["hostname"], device_id, k, interface["id"])


def del_device(name):

    url = base_url + "/dcim/devices/" + name + "/"
    response = requests.delete(url, headers=headers, verify=False)

    input(f"\nStatus code: {response.status_code}")


if __name__ == "__main__":

    # Loops until user exits
    while True:
        os.system("clear")
        choice = input("""Netbox API 2.9\n-------------------\n1. Add Site
2. Add Vendor \n3. Add Role \n4. Add Device Type \n5. Add Devices
6. Get Devices\n7. Delete Device\nSelect: """)

        # Add site
        if choice == "1":

            site = input("\n\nSite Name: ")
            add_site(site, site)

        # Add vendor
        elif choice == "2":

            models, vendors = main_getter()

            for vendor in vendors:
                add_vendor(vendor, vendor)

        # Add role
        elif choice == "3":

            name = input("\n\nRole: ")
            desc = input("Description: ")
            add_role(name, name, desc)

        # Add device type
        elif choice == "4":

            model, vendor = main_getter()
            vendor_getter()

            for model in models:
                for k, v in model.items():
                    id = input(f"\nManufacturer ID for device {k}")
                    add_device_type(id, v, v)

        # Add device
        elif choice == "5":

            with open("hosts.yaml", "r") as f:
                sources = yaml.safe_load(f)

            for k, v in sources.items():

                print(f"\n\nAdd device: {k}\n------------------------------\n")

                site_getter()
                site = input("\nSite ID: ")
                print("\n")
                type_getter()
                vendor = input("\nDevice Type ID: ")
                print("\n")
                role_getter()
                model = input("\nModel ID: ")
                print("\n")

                add_device(site, k, vendor, model)
        elif choice == "6":

            # Get request to query all devices and stores to variable devices
            devices = device_getter()
            print("\n\nDevices\n------------------------------\n")
            for device in devices:
                print(f"{device['id']}. {device['name']}")
            input("")
        elif choice == "7":

            # Get request to query all devices and stores to variable devices
            devices = device_getter()
            print("\n\nDevices\n------------------------------\n")
            for device in devices:
                print(f"{device['id']}. {device['name']}")
            choice = input("Device ID: ")
            del_device(choice)
