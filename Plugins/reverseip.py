
from requests import get
import re
from urllib.parse import urljoin, quote


def ReverseIP(host, port):
    # Validate host: allow only valid IP addresses or domain names
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    domain_pattern = re.compile(r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)"
                                r"(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?$")

    if not (ip_pattern.match(host) or domain_pattern.match(host)):
        print('Invalid IP address or domain name')
        return

    # Whitelist of allowed hosts (example: only allow specific domains or IPs)
    allowed_hosts = [
        '8.8.8.8',
        '8.8.4.4',
        'example.com',
        'api.hackertarget.com'
    ]

    # Check if the host is in the whitelist
    if host not in allowed_hosts:
        print('Host not allowed')
        return

    base_url = 'https://api.hackertarget.com/reverseiplookup/'
    # Safely construct URL with query parameter
    lookup = urljoin(base_url, '?q=' + quote(host))
    try:
        result = get(lookup).text
        print(result)
    except Exception:
        print('Error fetching data from API')
