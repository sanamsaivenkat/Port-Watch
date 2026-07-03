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
    try:
        start_port=int(input("Enter the starting port(eg: 75): "))
        end_port=int(input("Enter the ending port(eg: 95): "))
        if start_port>end_port or start_port<1 or end_port>65535:
            print("[!] Invalid port range configuration. Exiting.")
            sys.exit()
        print("_"*40)
        print(f"[*] Scanning started on {resolved_ip}....")
        print("[*] Please wait...")
        print("_"*40)

        for port in range(start_port,end_port+1):
            scan_single_port(resolved_ip,port)
        print("\n[+] Scan completed successfully.")
    except ValueError:
        print("[!]Error: ports must be whole numbers. Exiting.")
        sys.exit()