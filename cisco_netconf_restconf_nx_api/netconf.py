#!/usr/bin/env python3


from ncclient import manager
import xmltodict
import time
from loadfile import setdir
import signal

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Calls function to set current working directory to txtfiles
setdir()

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name></name>
        <description></description>
        <enabled></enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
              <address>
                    <ip></ip>
                    <netmask></netmask>
              </address>
         </ipv4>
    </interface>
  </interfaces>
</filter>"""

with open("cisco-ios-xe-list") as f:
    device = f.read().strip().splitlines()

start = time.perf_counter()
# Open a connection to the network device using ncclient
for hostname in device:

    print("Opening NETCONF Connection to ", hostname)
    m = manager.connect(
        host=hostname,
        port="10000",
        username="developer",
        password="C1sco12345",
        hostkey_verify=False,
    )

    print("Sending a <get-config> operation to the device", hostname)
    # Makes a NETCONF <get-config> query using the netconf_filter
    m_reply = m.get_config("running", netconf_filter)
    # Parses the returned XML to an Ordered Dictionary
    m_reply_dict = xmltodict.parse(m_reply.xml)["rpc-reply"]["data"]
    # Creates a list of interfaces
    interfaces = m_reply_dict["interfaces"]["interface"]

    for interface in interfaces:
        # Returns interface, status, description
        if "description" in interface:
            print(
                "Interface Name: {}, Enabled: {}, Description: {}".format(
                    interface["name"],
                    interface["enabled"],
                    interface["description"],
                )
            )
        else:
            print(
                "Interface Name: {}, Enabled: {}, Description: None, ".format(
                    interface["name"], interface["enabled"]
                )
            )
        # Returns ip and netmask
        try:
            address = interface["ipv4"]["address"]
            # Checks if  multiple IPs are configured
            if type(address) == list:
                for addr in address:
                    print(
                        "\t\tIP/Netmask: {}/{}".format(
                            addr["ip"], addr["netmask"]
                        )
                    )
            else:
                ipaddr = interface["ipv4"]["address"]["ip"]
                netmask = interface["ipv4"]["address"]["netmask"]
                print("\t\tIP/Netmask: {}/{}".format(ipaddr, netmask))
        except KeyError:
            print("\t\tIP: None, Netmask: None")

finish = time.perf_counter()

print("\n\nFinished in", round(finish - start, 3), "second(s)\n\n")
