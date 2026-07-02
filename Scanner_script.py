import socket
import sys

def validate_and_resolve_target():
    print("=== PortWatch Scanner ===")
    target=input("Enter target domain or IP(eg: google.com): ").strip()

    #if user jst hits enter without typing anything.This script shouldn't try to lookup a blank target. this stopr it immediately.
    if not target:
        print("[!] Error: Target cannot be empty.")
        sys.exit()
    try:
        print(f"[*] Resolving Target: {target}....")
        #using socket phonebook to get the IP of the target
        target_ip=socket.gethostbyname(target)

        print(f"[*] Successffully resolved targget IP address: {target_ip}....")
        print("-" * 40)
        return target_ip
    except socket.gaierror:
        print("[!] Error: Could not resolve host. check your spelling or Internet connection.")
        sys.exit()
def scan_single_port(target_ip,port):
    try:
        #create an ipv4 tcp socket
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #set 1-sec timelimit
        s.settimeout(1.0)
        #attempt to connect with target and specified port
        result=s.connect_ex((target_ip,port))
        #interrupt error code result
        if result==0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
        #Cleanup the socket connection resource
        s.close()
    except Exception as e:
        print(f"[!] System error scanning port {port}: {e}")
if __name__=="__main__":
    resolved_ip=validate_and_resolve_target()
    #Let's test our connection engine explicitly on Port 80 (Standard Web traffic)
    print(f"[*] Initiating Day 3 connection test on port 80...")
    scan_single_port(resolved_ip, 80)