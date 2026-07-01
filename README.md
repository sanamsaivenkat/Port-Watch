# PortWatch

A lightweight, beginner-friendly Network Port Scanner and Banner Grabber written in Python.
## Day 1 
Today , i have created the repo and add description and planned day 2.

## 🧠 What I Learned Today (Day 2)
Today, I focused on **Target Scoping and Name Resolution**. Before a scanner can interact with a target, it must convert human-readable names into network-routable formats:
- **DNS Resolution (`socket.gethostbyname`)**: I learned that computers communicate using IP addresses at the Network Layer, not domain names. This function queries DNS servers to translate domains (like `scanme.nmap.org`) into IP addresses.
- **Input Guardrails**: Added checks to handle empty inputs cleanly so the script doesn't waste resources trying to resolve a blank target.
- **Exception Handling (`socket.gaierror`)**: Security tools must be resilient. I implemented `try/except` blocks to catch invalid domains or network disconnections gracefully instead of letting the program crash.
