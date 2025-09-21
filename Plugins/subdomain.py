
import json
import requests
import socket

# Define a whitelist of allowed domains to prevent SSRF
ALLOWED_DOMAINS = [
    'example.com',
    'trusted.com',
    'virustotal.com'
]

def is_allowed_domain(host):
    # Check if the host ends with any of the allowed domains
    host = host.lower().strip()
    for domain in ALLOWED_DOMAINS:
        if host == domain or host.endswith('.' + domain):
            return True
    return False


def SubDomain(host, port):

    # Validate that host is a valid domain name or IP address
    try:
        # Attempt to resolve the host to an IP address to ensure validity
        resolved_ip = socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError(f"Invalid host provided: {host}")

    # Enforce whitelist check to mitigate SSRF
    if not is_allowed_domain(host):
        raise ValueError(f"Host not allowed: {host}")

    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {'apikey':'1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}

    response = requests.get(url, params=params)

    subdomains = response.json()

    for x in subdomains.get('domain_siblings', []):
        print(x)

