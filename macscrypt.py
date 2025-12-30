# Functionality: Changes the MAC address of supplied interface with randomly generated MAC address.

import random, subprocess

# Defining the functionality of the program
print("Script changes MAC address of current machine to randomly generated address")

# Supply interface of MAC address to be changed
interface = input("Supply interface to change MAC address: ")

# Generating random MAC address for NIC card.
random_mac = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Printing the random MAC address and interface
print("Generated Random MAC: " + random_mac)
print("Changing " + interface + " to random MAC of " + random_mac)

# Change the MAC address using subprocess library
# Setting supplied interface to DOWN status

subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])

# Change supplied interface to generated mac address.
subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", random_mac])

# Setting supplied interface back to UP status
subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])

#print final result
print("interface " + interface + " Mac address has been changed to: " + random_mac)
