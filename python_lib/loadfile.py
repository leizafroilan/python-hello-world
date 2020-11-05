#!/usr/bin/env python3

import os


# Function to set working directory to txtfiles
def setdir():

    path = os.environ.get("workdir")
    os.chdir(path)


# Function to overwrite new_config.cfg
def write_cmd():

    os.system("clear")

    print('***Type "exit" to end  edit and save file***')
    print("Enter commands here: \n\n")

    with open("new_config.cfg", "w+") as outf:
        # Loops and saves input to new_config.cfg while input is not "exit"
        while True:
            lines = input()
            if lines == "Exit".lower():
                os.system("clear")
                break
            else:
                outf.write("\n")
                outf.write(lines)


# Function to load list of devices
def select_device():

    deviceDict = {}

    os.system("clear")

    with open("H-list") as f:
        devices = f.read().splitlines()

    devices = filter(None, devices)

    for index, device in enumerate(devices, start=1):

        deviceDict[index] = device
        print("{}. {}".format(index, device))

    selected = int(input("Select device to configure(CTRL+C to exit): "))

    os.system("clear")
    hostname = deviceDict[selected]

    return hostname


# Function to compare running and candidate config
def diff(diffs, cisco_ios):

    try:
        if len(diffs) > 0:
            print(diffs)
            print("Saving configuration")
            cisco_ios.commit_config()
            print("Configuration has been saved")
            input("\n\n<<<Press Enter to continue>>>")

        else:
            print("No configuration changes required.")
            cisco_ios.discard_config()
            input("\n\n<<<Press Enter to continue>>>")
    except:
        print("Invalid Configuration")
        input("\n\n<<<Press Enter to continue>>>")


def select_command():

    commandDict = {}

    os.system("clear")

    with open("napalm-cmds") as f:
        commands = f.read().splitlines()

    commands = filter(None, commands)

    for index, command in enumerate(commands, start=1):

        commandDict[index] = command
        print("{}. {}".format(index, command))

    selected = int(input("Enter command(CTRL+C to exit): "))

    os.system("clear")
    cmd = commandDict[selected]

    return cmd
