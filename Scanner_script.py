import socket
import sys
target=input("Enter target domain or IP: ").strip()

#if user jst hits enter without typing anything.This script shouldn't try to lookup a blank target. this stopr it immediately.
if not target:
    print("[!] Error: Target cannot be empty.")
    sys.exit()
try:
    print(f"[*] Resolving Target: {target}....")
    #using socket phonebook to get the IP of the target
    target_ip=socket.gethostbyname(target)

    print(f"[*] Target IP address: {target_ip}....")
except socket.gaierror:
    print("[!] Error: Could not resolve host. check your spelling or Internet connection.")
    sys.exit()
