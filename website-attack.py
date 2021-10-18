import subprocess
import socket
from time import sleep
x  = input("Enter website : ")

ip = socket.gethostbyname(x)

subprocess.run(["nmap" , f"{ip}" , "-Pn"])
print("-")
print("\033[92m {}\033[00m" .format('[-] Nmap Done'))
print("-")
sleep(2)


subprocess.run(["whois" , f"{x}"])

print("-")
print("\033[92m {}\033[00m" .format('[-] whois Done'))
print("-")
sleep(2)

print("\033[91m {}\033[00m" .format(' [-] Sn1per now will start \n ( CTRL + X for EXIT '') '))
sleep(2)

print("----")
print("Enter the mode")
print("----")
print("\033[92m {}\033[00m" .format('1 - NORMAL MODE'))
print("\033[93m {}\033[00m" .format('2- NORMAL MODE + OSINT + RECON'))
print("\033[93m {}\033[00m" .format('3 - STEALTH MODE + OSINT + RECON'))

modnum = input("Enter mode number : ")

if modnum == "1":
	subprocess.run([ "sniper", "-t" , f"{ip}"])

elif modnum == "2":
	subprocess.run(["sniper" , "-t" , f"{ip}" , "-o" , "-re"])
elif modnum == "3":
	subprocess.run(["sniper" , "-t" , f" {ip}" , "-m" , "stealth" , "-o" , "-re"])
else:
	subprocess.run(["sniper" , "-t" , f"--help"])
