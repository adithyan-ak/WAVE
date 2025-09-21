
from requests import get
import re


def ReverseIP(host, port):
    # Validate host: allow only valid IP addresses or domain names
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    domain_pattern = re.compile(r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)" 
                                r"(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?$")

    if not (ip_pattern.match(host) or domain_pattern.match(host)):
        print('Invalid IP address or domain name')
        return

    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(result)
    except Exception:
        print('Error fetching data from API')
