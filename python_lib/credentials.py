from getpass import getpass


def uid():
    # Prompt for username/password
    username = input("Username: ")

    return username


def pw():
    password = None
    # Verify if password matches
    while not password:
        password = getpass()
        password1 = getpass("Re-type Password: ")
        if password != password1:
            print("Try again")
            password = None

    return password
