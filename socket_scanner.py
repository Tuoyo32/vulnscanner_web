# socket_scanner.py

import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def scan_ports(target):
    open_ports = []
    for port, service in COMMON_PORTS.items():
        try:
            sock = socket.create_connection((target, port), timeout=1)
            sock.close()
            open_ports.append(f"TCP {port} - open ({service})")
        except:
            pass
    return open_ports
