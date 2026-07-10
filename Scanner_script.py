import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# Well-known infrastructure port fallbacks
common_ports={
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 3389: "RDP"
}

def validate_and_resolve_target():
    """
    Prompts the user for a target and performs DNS resolution.
    Returns a tuple of (target_ip, original_input_string).
    """
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
        return target_ip, target
    except socket.gaierror:
        print("[!] Error: Could not resolve host. check your spelling or Internet connection.")
        sys.exit()
def scan_single_port(target_ip,port,storage_list):
    """
    Probes an explicit TCP port channel.
    Resolves application layer service mappings and grabs application banners.
    Saves discovered assets dynamically into the provided storage list.
    """
    try:
        #create an ipv4 tcp socket
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #set 1-sec timelimit
        s.settimeout(0.5)
        #attempt to connect with target and specified port
        result=s.connect_ex((target_ip,port))
        #interrupt error code result
        if result==0:
            try:
                # This queries your computer's OS database for the official name
                service_name=socket.getservbyport(port,"tcp").upper()
            except (OSError,OverflowError):
                # Fallback to our custom list if the OS doesn't recognize it
                service_name=common_ports.get(port,"unknown service")
            print(f"[+] Port {port} ({service_name}): OPEN")

            banner_line=""
            try:
                # Attempt to grab the service banner
                # We listen for up to 1024 bytes of data
                raw_banner=s.recv(1024)
                if raw_banner:
                    # Decode the raw bytes into a standard text string
                    clean_banner=raw_banner.decode(errors='ignore').strip()
                    banner_line=f"    [->] Banner Detected: {clean_banner}"
                else:
                    banner_line="    [->] Banner: No response(Service is quiet)"
            except socket.timeout:
                # some ports are open but won't talk until you speak first
                banner_line="    [->] Banner: Timeout(Service requires a request)"
            print(banner_line)
            #Save the result into our list so we can log it to a file later
            # Appending safely directly into the locally passed tracking list
            storage_list.append((port,service_name,banner_line.strip()))
        s.close()
        # else:
        #     print(f"[-] Port {port}: CLOSED")
        # #Cleanup the socket connection resource
        # s.close()
    except (socket.timeout, ConnectionRefusedError, OSError):
        # Day 7 Upgrade: Quietly drop expected socket failures on closed/filtered ports
        pass
    except Exception as e:
        # Day 7 Upgrade: Safely capture true system runtime errors without crashing the thread pool
        print(f"\n[!] Unexpected worker exception on port {port}: {e}")
def save_report(filename,target,target_ip,start_port,end_port,findings):
    """
    Handles report compilation File I/O tasks natively.
    Sorts findings and dumps them into a structured text document.
    """
    print("[*] Generating report file...")
    with open("scan_report.txt", "w") as report:
        report.write("========================================\n")
        report.write("          PORTWATCH SCAN REPORT         \n")
        report.write("========================================\n")
        report.write(f"Target Host: {target} ({target_ip})\n")
        report.write(f"Scanned Range: {start_port} - {end_port}\n")
        report.write("----------------------------------------\n\n")
        if findings:
            findings.sort()
            for port,service, banner in findings:
                report.write(f"[+] Port {port} ({service}): OPEN\n")
                report.write(f"     {banner}\n\n")
        else:
            print("[-] No open ports discovered within the scanned range.\n")
        report.write("\n========================================\n")
        report.write("Scan terminated cleanly.\n")
            
    print(f"[+] Success! Report saved to {filename}.")

def main():
    resolved_ip,original_target=validate_and_resolve_target()
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
        # Isolated memory collection list (No longer a global threat
        scan_findings=[]

        with ThreadPoolExecutor(max_workers=50) as executor:
            for port in range(start_port,end_port+1):
                executor.submit(scan_single_port, resolved_ip, port,scan_findings)
        print("\n[+] Scan completed successfully.")
        # Trigger the newly isolated report module
        save_report("scan_report.txt",original_target,resolved_ip,start_port,end_port,scan_findings)
        
    except ValueError:
        print("[!]Error: ports must be whole numbers. Exiting.")
        sys.exit()
if __name__=="__main__":
    main()