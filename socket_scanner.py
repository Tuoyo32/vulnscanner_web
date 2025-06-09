import socket

def basic_scan(host):
    open_ports = []
    for port in range(20, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        except Exception:
            continue
    return open_ports
