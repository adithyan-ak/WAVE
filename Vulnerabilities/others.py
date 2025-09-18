from urllib.request import *
from urllib.parse import urlparse
import socket


ALLOWED_DOMAINS = ['www.skcet.ac.in', 'skcet.ac.in']


def is_valid_host(host):
    try:
        # Parse host to ensure it's a valid hostname or IP
        parsed = urlparse('http://' + host)
        hostname = parsed.hostname
        if not hostname:
            return False

        # Check if host is in allowed domains (exact match or subdomain)
        for domain in ALLOWED_DOMAINS:
            if hostname == domain or hostname.endswith('.' + domain):
                # Resolve hostname to IP and check if it's public
                ip = socket.gethostbyname(hostname)
                # Simple check to avoid private IPs (RFC1918)
                if ip.startswith('10.') or ip.startswith('192.168.') or ip.startswith('172.'):
                    return False
                return True
        return False

    except Exception:
        return False


def OpenRedirect(host, port):
    if not is_valid_host(host):
        print(f"Invalid or disallowed host: {host}")
        return

    if port == 80:
        scheme = 'http://'
    elif port == 443:
        scheme = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
        return

    print('Testing with all available payloads')

    i = 2

    url = (scheme + host)
    q = Request(url)
    q.add_header('X-Forwarded-Host', 'https://google.com')
    try:
        a = urlopen(q).getcode()
    except Exception:
        print("Error opening URL with X-Forwarded-Host header")
        a = None

    if a == 302:
        print("Testing Payload 1 : Vulnerable to X-Forwarded-Host Header")
    else:
        print('Testing Payload 1 : Not Vulnerable')

    try:
        with open("redirectpayloads.txt", "r") as f:
            f1 = f.readlines()
    except Exception:
        print("Error reading redirectpayloads.txt")
        return

    for x in f1:
        x = x.strip()
        while i < 34:
            try:
                test_url = scheme + host + x
                data = urlopen(test_url)
                code = data.getcode()
            except Exception:
                print(f"Testing Payload {i} : Error")
                break

            if code == 302:
                print(f"Testing Payload {i} : Vulnerable")
                print(test_url)
                break
            elif code == 200:
                print(f"Testing Payload {i} : Not Vulnerable")
                break
            else:
                print(f"Testing Payload {i} : Not Vulnerbale")
                break

        i += 1


OpenRedirect('www.skcet.ac.in', 80)