import nmap

def scan_with_nmap(target):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=target, arguments='-T4 -F')
        result = {}
        for host in nm.all_hosts():
            result[host] = []
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    result[host].append(f"{proto.upper()} {port} - {nm[host][proto][port]['state']}")
        return result
    except Exception as e:
        return {"error": str(e)}
