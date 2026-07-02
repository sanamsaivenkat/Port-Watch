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
