import socket
import platform
import uuid
import subprocess
from datetime import datetime

print("=" * 50)
print("SECURE NETWORK ASSET INVENTORY")
print("=" * 50)

# Hostname
hostname = socket.gethostname()

# Local IP address
try:
    local_ip = socket.gethostbyname(hostname)
except socket.error:
    local_ip = "Unable to determine"

# MAC address
mac = uuid.getnode()
mac_address = ":".join(
    f"{(mac >> i) & 0xff:02x}" for i in range(40, -1, -8)
)

# Operating system information
os_info = platform.platform()

# Network interfaces
try:
    interfaces = subprocess.check_output(
        ["ip", "-br", "addr"], text=True
    )
except Exception:
    interfaces = "Unable to retrieve network interfaces"

# Display information
print(f"Hostname        : {hostname}")
print(f"Local IP        : {local_ip}")
print(f"MAC Address     : {mac_address}")
print(f"Operating System: {os_info}")

print("\nActive Network Interfaces:")
print(interfaces)

# Save report
report = f"""
SECURE NETWORK ASSET INVENTORY
Generated: {datetime.now()}

Hostname:
{hostname}

Local IP:
{local_ip}

MAC Address:
{mac_address}

Operating System:
{os_info}

Active Network Interfaces:
{interfaces}
"""

with open("system_report.txt", "w") as file:
    file.write(report)

print("Report saved as: system_report.txt")
