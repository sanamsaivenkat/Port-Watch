# 🔍 PortWatch

PortWatch is a high-speed, multi-threaded network reconnaissance tool written in Python. Designed for security analysts and network administrators, it performs rapid TCP port scanning, maps active ports to known system services, extracts application layer banner signatures, and compiles structural audit reports.



---

## 🚀 Core Features

* ⚡ **High-Speed Execution Engine**: Leverages a synchronized `ThreadPoolExecutor` framework allocating 50 background workers to probe hundreds of ports simultaneously.
* 🧠 **Hybrid Service Mapping**: Queries local operating system service databases (`socket.getservbyport`) dynamically with an integrated hardcoded dictionary fallback for non-standard ports.
* 🛡️ **Resilient Fault Isolation**: Suppresses expected network timeouts and connection resets quietly, preventing worker thread pool degradation during wide-range firewall scans.
* 📋 **Automated Audit Logging**: Consolidates asynchronous thread findings into a structured, numerically sorted local text report (`scan_report.txt`).

---

## 🛠️ Installation & Requirements

PortWatch relies exclusively on native Python standard libraries, meaning **zero external third-party dependencies** are required to run the tool.

### Prerequisites
* Python 3.x installed on your host operating system.

### Setup
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/sanamsaivenkat/PortWatch.git](https://github.com/sanamsaivenkat/PortWatch.git)
   cd PortWatch

2.Launch the utility:

Bash
python Scanner_script.py

3.Terminal Interface(Output preview):

=== PortWatch Scanner ===
Enter target domain or IP (eg: google.com): test.rebex.net
[*] Resolving Target: test.rebex.net....
[*] Successfully resolved target IP address: 195.144.107.198....
----------------------------------------
Enter the starting port (eg: 20): 21
Enter the ending port (eg: 25): 23
________________________________________
[*] Scanning started on 195.144.107.198 using 50 parallel workers....
[*] Please wait...
________________________________________
[+] Port 21 (FTP): OPEN
    [->] Banner Detected: 220 RebexFTP/1.0.3.0 FTP server ready
[+] Port 22 (SSH): OPEN
    [->] Banner Detected: SSH-2.0-RebexSSH_5.0.8712.0

[+] Scan completed successfully.
[*] Generating report file...
[+] Success! Report saved to 'scan_report.txt'.

->Generated scan_report.txt

========================================
          PORTWATCH SCAN REPORT         
========================================
Target Host: test.rebex.net (195.144.107.198)
Scanned Range: 21 - 23
----------------------------------------

[+] Port 21 (FTP): OPEN
    Banner Detected: 220 RebexFTP/1.0.3.0 FTP server ready

[+] Port 22 (SSH): OPEN
    Banner Detected: SSH-2.0-RebexSSH_5.0.8712.0

========================================
Scan terminated cleanly.

10-Day Engineering Journey
This tool was systematically developed over a 10-day agile engineering cycle to master low-level network socket layers and asynchronous execution patterns:

Day 1: Repository instantiation, architectural blueprints, and target configuration workflows.

Day 2: Sanitization engines, boundary input controls, and system failure exceptions.

Day 3: Low-level TCP socket stream initialization and connection handling configurations.

Day 4: Iterative range scanning algorithms and network parameter boundary controls.

Day 5: Dynamic application layer banner signature extraction and timeout catch blocks.

Day 6: IANA protocol identification and systemic OS network translation integrations.

Day 7: Concurrency scaling using abstracted asynchronous ThreadPoolExecutor workers.

Day 8: Structured file system streams and persistent data capture layers.

Day 9: Code refactoring, global state eradication, and clean modular decoupling.

Day 10: Production repository documentation compilation and deployment testing.

⚠️ Disclaimer: This tool is designed explicitly for authorized security auditing, educational research, and internal network maintenance. Probing external infrastructures without explicit written consent is illegal.
