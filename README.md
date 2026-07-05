# PortWatch

A lightweight, beginner-friendly Network Port Scanner and Banner Grabber written in Python.
## Day 1 
Today , i have created the repo and add description and planned day 2.

## 🧠 What I Learned Today (Day 2)
Today, I focused on **Target Scoping and Name Resolution**. Before a scanner can interact with a target, it must convert human-readable names into network-routable formats:
- **DNS Resolution (`socket.gethostbyname`)**: I learned that computers communicate using IP addresses at the Network Layer, not domain names. This function queries DNS servers to translate domains (like `scanme.nmap.org`) into IP addresses.
- **Input Guardrails**: Added checks to handle empty inputs cleanly so the script doesn't waste resources trying to resolve a blank target.
- **Exception Handling (`socket.gaierror`)**: Security tools must be resilient. I implemented `try/except` blocks to catch invalid domains or network disconnections gracefully instead of letting the program crash.

## 🧠 What I Learned Today (Day 3)
Today, I built the core scanning engine using Python's `socket` library. I learned how the **TCP Three-Way Handshake** works under the hood for reconnaissance:
- **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**: Initializes a fresh network connection pathway configured for IPv4 and the TCP protocol.
- **`s.settimeout(1.0)`**: Crucial for tool performance. Prevents the scanner from getting stuck hanging indefinitely if a remote target is hidden behind an aggressive network firewall.
- **`s.connect_ex()`**: Performs a low-level handshake knock on the port. If it catches a return value of `0`, the socket successfully established a connection (**Port is OPEN**). Any other error number indicates the port is closed or filtered.
- **Resource Management**: I learned that every opened socket connection must be explicitly terminated with `s.close()` to avoid operating system memory leaks.

## 🧠 What I Learned Today (Day 4)
Today, I advanced the single-port script into a true **Port Range Scanner** by introducing looping control structures:
- **`for port in range(start, end + 1)`**: I learned that Python's `range()` function is exclusive of the upper bound. Adding `+ 1` ensures that the final port selected by the user is actually scanned.
- **Data Type Conversion**: Since user inputs via `input()` are strictly string data types, I utilized `int()` to explicitly convert inputs into integers so they work natively with network port calculations.
- **UI Optimization**: Modified the connection engine to suppress logging "CLOSED" ports. This keeps the terminal clear and highlights only actionable intelligence (**OPEN** ports).
- **Linear Time Complexity**: Observed that scanning sequentially scales execution time linearly ($O(n)$) based on the size of the port range, setting up the exact performance issue I will solve later with multi-threading.

## 🧠 What I Learned Today (Day 5)
Today, I advanced the scanner from simple port detection to **Application Exposure Assessment** via Banner Grabbing:
- **Service Enumeration**: I learned that open ports run background software that broadcasts a greeting string (banner) upon connection. Capturing this helps security analysts identify software names and exact versions to map potential CVE vulnerabilities.
- **Data Stream Catching (`s.recv(1024)`)**: Implemented a data buffer constraint to capture up to 1024 bytes of raw binary data directly from the active network socket channel.
- **Data Normalization (`.decode(errors='ignore')`)**: Networks transmit raw bytes. I utilized string decoding configurations to format network traffic into clean, readable text strings while bypassing unmapped security characters.
- **Nested Timeout Protections**: Learned that many defensive services or standard web servers (like Google on Port 80) remain silent until a valid client payload is sent. Handling `socket.timeout` within the execution tree prevents quiet services from breaking scanner flow.

## 🧠 What I Learned Today (Day 6)
Today, I implemented **Service Mapping and Asset Identification** to translate raw numbers into meaningful intelligence:
- **IANA Port Protocol Standards**: Learned that ports 0-1023 are "Well-Known Ports" reserved for fundamental structural services (like SSH, HTTP, and HTTPS).
- **Dynamic OS Database Queries (`socket.getservbyport`)**: Instead of hardcoding thousands of ports manually, I leveraged native OS lookup functions to query the local network services translation layer dynamically.
- **Failover Logic (Dictionary Backups)**: Created a hybrid lookup model. The tool first queries the system database; if the service is non-standard or unregistered, it gracefully drops back to a custom Python dictionary map or defaults cleanly to an "Unknown Service" string.