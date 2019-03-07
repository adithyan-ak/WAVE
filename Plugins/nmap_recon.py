import nmap
import json

def Nmap_Recon(host, port):
    nm = nmap.PortScanner()
    lol = nm.scan(host, '22-443')
    ip = dict.keys(lol['scan'])
    list(ip)
    ip_addr = (list(ip)[0])
    print("IP Address : %s" % ip_addr)
    json_scan = json.dumps(lol['scan'])
    parsed = json.loads(json_scan)
    print(json.dumps(parsed, indent=4, sort_keys=True))
