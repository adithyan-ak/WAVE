
from requests import get
import ipaddress
import re


def is_valid_domain(domain):
    # Simple regex for domain validation (RFC 1035 compliant simplified)
    pattern = re.compile(
        r'^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)'
        r'(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?'  # allow trailing dot
    )
    return pattern.match(domain) is not None


def ReverseIP(host, port):
    # Validate host: allow only valid IP addresses or domains
    try:
        # Check if host is a valid IP address (IPv4 or IPv6)
        ipaddress.ip_address(host)
        valid_host = True
    except ValueError:
        # If not IP, check if valid domain
        valid_host = is_valid_domain(host)

    if not valid_host:
        print('Invalid IP address or domain')
        return

    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(result)
    except Exception:
        print('Invalid IP address')
