import requests
import re
import socket


def Lfi(domain, port):
    # Validate domain to allow only valid domain names or IP addresses
    domain_pattern = re.compile(r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$')
    ip_pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}$')
    if not (domain_pattern.match(domain) or ip_pattern.match(domain)):
        raise ValueError("Invalid domain format")

    # Additional SSRF protection: resolve domain and check against private IP ranges
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        raise ValueError("Domain name could not be resolved")

    # Disallow private and reserved IP ranges
    private_ranges = [
        ('10.0.0.0', '10.255.255.255'),
        ('172.16.0.0', '172.31.255.255'),
        ('192.168.0.0', '192.168.255.255'),
        ('127.0.0.0', '127.255.255.255'),
        ('169.254.0.0', '169.254.255.255'),
        ('0.0.0.0', '0.255.255.255'),
        ('224.0.0.0', '239.255.255.255'),
        ('240.0.0.0', '255.255.255.254'),
        ('255.255.255.255', '255.255.255.255')
    ]

    def ip_to_int(ip):
        return int.from_bytes(socket.inet_aton(ip), 'big')

    ip_int = ip_to_int(ip_address)
    for start, end in private_ranges:
        if ip_to_int(start) <= ip_int <= ip_to_int(end):
            raise ValueError("Domain resolves to a private or reserved IP address")

    payload = {'key': '1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66', 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    return response
