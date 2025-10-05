
import nmap
import json


def DefaultPort(Xhost, Yport):
    print('')
    print("Starting port scan with range 22-443")
    nm = nmap.PortScanner()
    result = nm.scan(Xhost, '22-443')
    display(result)


def Customrange(Xhost, Yport):
    print('')
    port_range = input("Enter the range : ")
    # Validate port_range format: must be start-end with ports between 1 and 65535
    def is_valid_port_range(pr):
        if '-' not in pr:
            return False
        parts = pr.split('-')
        if len(parts) != 2:
            return False
        try:
            start = int(parts[0])
            end = int(parts[1])
            if 1 <= start <= 65535 and 1 <= end <= 65535 and start <= end:
                return True
            else:
                return False
        except ValueError:
            return False
    if not is_valid_port_range(port_range):
        print('Invalid port range input. Using default range 22-443.')
        port_range = '22-443'
    print('')
    print("Starting port scan with range %s" % port_range)
    nm = nmap.PortScanner()
    result = nm.scan(Xhost, port_range)
    display(result)


def display(result):
    new = next(iter(result['scan'].values()))
    ip_add = new['addresses']
    print('')
    print("IP Address : %s" % ip_add['ipv4'])
    hosting = new['hostnames']
    hostname0 = hosting[0]
    hostname1 = hosting[1]
    print('')
    print("Hostname 1  : %s" % hostname0['name'])
    print("Hostname 2  : %s" % hostname1['name'])
    print('')
    print("Open Ports  : ")
    print('')
    ports = new['tcp']
    json_scan = json.dumps(ports)
    parsed = json.loads(json_scan)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    print('')
