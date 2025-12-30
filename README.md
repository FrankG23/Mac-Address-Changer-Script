# Mac-Address-Changer-Script
EDUCATIONAL PURPOSES ONLY

Developed a Python-based network scanner to identify active devices on a local network and map IP addresses to MAC addresses using ARP discovery. Designed for defensive security use cases such as asset visibility, network auditing, and detection of unauthorized devices.


Showing how to 'Manually' change your MAC using Kali Linux as demonstration
<img width="784" height="622" alt="Pasted image 20251225001712" src="https://github.com/user-attachments/assets/94f565ea-8388-4ea7-9862-ddcc7552cc0c" />

 Here is a showcase of showing current VM's Mac address , than setting our network operational status to 'Down'. This step is crucial for spoofing your mac address 


<img width="780" height="395" alt="Pasted image 20251225002044" src="https://github.com/user-attachments/assets/76690f55-ec51-4c59-b3c0-a9101996f3cf" />

Now here I have used sudo ip link set dev eth0 address 08:02:27:00:00:00 (completely random) to set my 'new' mac address and showing that it indeed did change.
In fact this was very simple to do , all with some simple commands that anyone can take the time and look up if needed.
Mac Spoofing bypasses network security , access restricted Wi-Fi, or hide identity, or even impersonate other devices, used for both malicious reasons like unauthorized network entry and legitimate purposes like troubleshooting or network  redundancy. It tricks system into thinking a spoofed device is a trusted one, which enables attackers to eavesdrop or gain access, while administrators use it for testing and failover systems 

---

Now the main project I thought of doing was turning this into a script itself
- <img width="1279" height="799" alt="Pasted image 20251225014315" src="https://github.com/user-attachments/assets/d8172998-0a8e-4937-932c-f45c6f30a530" />
- For this portion I ended up creating a python script  as shown above

<img width="1212" height="97" alt="Pasted image 20251225014641" src="https://github.com/user-attachments/assets/7351a62d-5f45-45e7-9fb8-0eabb3d3ab89" />
- - We have showing original mac address prior to running the script
 
<img width="1217" height="396" alt="Pasted image 20251225014659" src="https://github.com/user-attachments/assets/07487002-1750-4898-b85f-36f6ebcabba9" />
- Than we have running the script and showing the mac address did in fact did change as intended to do so 
