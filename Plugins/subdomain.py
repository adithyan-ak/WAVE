
import json
import requests
import socket


def SubDomain(host, port):

    # Validate that host is a valid domain name or IP address
    try:
        # Attempt to resolve the host to an IP address to ensure validity
        resolved_ip = socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError(f"Invalid host provided: {host}")

    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {'apikey':'1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}

    response = requests.get(url, params=params)

    subdomains = response.json()

    for x in subdomains.get('domain_siblings', []):
        print(x)

