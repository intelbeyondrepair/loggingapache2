#!/usr/bin/python3
# Writen By: Intel.Beyond.Repair (Shawn Adams)
# This is a handy little script for quickly going through logs
#
import os
from time import sleep

# Prints Banner and Menu
def banner():
    print("""
		 _                  ____                _
		| |    ___   __ _  |  _ \ ___  __ _  __| | ___ _ __
		| |   / _ \ / _` | | |_) / _ \/ _` |/ _` |/ _ \ '__|
		| |__| (_) | (_| | |  _ <  __/ (_| | (_| |  __/ |
		|_____\___/ \__, | |_| \_\___|\__,_|\__,_|\___|_|
            		    |___/

                        """)
    print("""
    	     1) View Recent SSH logins.
    	     2) View All Sudo Auth Logs.
             3) View Recent Apache2 Access Requests.
    	     4) View Kernel Messages.
    	     5) Exit.""")


# Prints Successful SSH Login Attempts.
def sshlogins():
    os.system("gnome-terminal -e 'bash -c \"cat /var/log/auth.log | grep \"Accepted\"; exec bash\"'")

def sshattempts():
    os.system("gnome-terminal -e 'bash -c \"cat /var/log/auth.log; exec bash\"'")

# Prints the Access Log of the Apache2 Server. (Requires Apache2 to be installed)
def apach():
    os.system("gnome-terminal -e 'bash -c \"cat /var/log/apache2/access.log; exec bash\"'")

# Prints the Kernel Messages using dmesg
def kernel():
    os.system("gnome-terminal -e 'bash -c \"dmesg; exec bash\"'")

# Main Function
def Main():
    # Clears the screen. Makes it look nice.
    os.system('clear')

    # Checks if user is Root. This script needs to be run as root.
    if os.geteuid() != 0:
        print("\n ERROR: Run as Root")
        os._exit(1)

    banner()

    try:
        # Takes user input and stores it in user_input.
        user_input = int(float(input("Logging@root -> ")))

        # If the user input equals to 1, Print the SSH Logins.
        if user_input == 1:
            sshlogins()
            Main()

        # If the user input equals to 2, Print the Sudo Auth Logs.
        if user_input == 2:
            sshattempts()
            Main()

        # If the user input equals to 3, Print the Apache2 Access Log.
        elif user_input == 3:
            apach()
            Main()

        # If the user input equals to 4, Print the Kernel Messages.
        elif user_input == 4:
            kernel()
            Main()

        # If the user input equals 5, Exit the script.
        elif user_input == 5:
            os._exit(1)

        # If User input equals anything else, print the menu again.
        else:
            sleep(5)
            Main()

    # If the User Input does not equal anything listed, it is invalid.
    except ValueError as err:
        print("Invalid Input")
        print(err)

# Starts the Main Function
if __name__ == '__main__':
    Main()
