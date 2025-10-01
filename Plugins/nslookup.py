
from requests import get
import re


# Simple whitelist regex for allowed hosts: domain names and IP addresses
WHITELIST_REGEX = re.compile(r'^(?:[a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+$|^(?:\d{1,3}\.){3}\d{1,3}$')

def nsLookup(host, port):
    # Validate host against whitelist regex
    if not WHITELIST_REGEX.match(host):
        raise ValueError('Invalid host provided')

    result = get('http://api.hackertarget.com/dnslookup/?q=' + host).text
    print(result)

host = 'www.skcet.ac.in'

