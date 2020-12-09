#!/usr/bin/env python3

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from headers import form_headers
import requests
import os

headers = form_headers()
base_url = "http://192.168.10.235/api"


# Runs Nornir to get all device models and device vendors
def main_getter():

    path = os.environ.get("workdir")
    os.chdir(path)

    results = []

    nr = InitNornir("config.yaml")

    hosts = nr.run(task=napalm_get, getters=["facts"])

    for host in hosts:
        # Executes if Nornir was able to query "get facts" to the device
        if not hosts[host].failed:
            result = hosts[host].result["facts"]
            results.append(result)

    # Creates lists for all models and vendors
    device_model = [{result["hostname"]: result["model"]} for result in results]
    device_vendor = [result["vendor"] for result in results]

    return device_model, device_vendor


# Gets all devices from Netbox - 192.168.10.235
def device_getter():

    url = base_url + "/dcim/devices/"
    response = requests.get(url, headers=headers, verify=False)
    devices = response.json()["results"]

    return devices


# Gets all interfaces from Netbox - 192.168.10.235
def interface_getter():

    url = base_url + "/dcim/interfaces/"
    response = requests.get(url, headers=headers, verify=False)
    interfaces = response.json()["results"]

    return interfaces


# Gets all vendors from Netbox - 192.168.10.235
def vendor_getter():

    url = base_url + "/dcim/manufacturers/"
    response = requests.get(url, headers=headers, verify=False)
    results = response.json()["results"]

    for result in results:

        print(f"{result['id']} {result['name']}")


# Gets all roles from Netbox - 192.168.10.235
def role_getter():

    url = base_url + "/dcim/device-roles/"
    response = requests.get(url, headers=headers, verify=False)
    results = response.json()["results"]

    for result in results:

        print(f"{result['id']}: {result['name']}")


# Gets all device types from Netbox - 192.168.10.235
def type_getter():

    url = base_url + "/dcim/device-types/"
    response = requests.get(url, headers=headers, verify=False)
    results = response.json()["results"]

    for result in results:

        print(f"{result['id']}: {result['model']}")


# Gets all sites from Netbox - 192.168.10.235
def site_getter():

    url = base_url + "/dcim/sites/"
    response = requests.get(url, headers=headers, verify=False)
    results = response.json()["results"]

    for result in results:

        print(f"{result['id']}: {result['name']}")
