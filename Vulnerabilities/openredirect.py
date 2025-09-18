from urllib.request import *
from urllib.parse import urlparse


def OpenRedirect(host, port):
    # Validate and sanitize host
    parsed_host = urlparse(host if '://' in host else '//' + host)
    if not parsed_host.hostname:
        print("Invalid host provided")
        return
    host = parsed_host.hostname

    # Validate and sanitize port
    if port == 80:
        scheme = 'http://'
    elif port == 443:
        scheme = 'https://'
    else:
        print("Couldn't fetch data for the given PORT")
        return

    # Define allowed hosts to prevent SSRF
    allowed_hosts = {host}

    print('Testing with all available payloads')

    i = 2

    base_url = scheme + host

    # Test X-Forwarded-Host header
    try:
        q = Request(base_url)
        q.add_header('X-Forwarded-Host', 'https://google.com')
        a = urlopen(q).getcode()
        if a == 302:
            print("Testing Payload 1 : Vulnerable to X-Forwarded-Host Header")
        else:
            print('Testing Payload 1 : Not Vulnerable')
    except Exception as e:
        print(f"Testing Payload 1 : Error ({e})")

    try:
        with open("redirectpayloads.txt", "r") as f:
            payloads = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading redirectpayloads.txt: {e}")
        return

    for x in payloads:
        if i >= 34:
            break

        # Construct URL and validate
        test_url = scheme + host + x
        parsed_url = urlparse(test_url)

        # Allow only URLs with the base host to prevent SSRF
        if parsed_url.hostname not in allowed_hosts:
            print(f"Testing Payload {i} : Skipped due to disallowed host")
            i += 1
            continue

        try:
            response = urlopen(test_url)
            code = response.getcode()
        except Exception as e:
            print(f"Testing Payload {i} : Error ({e})")
            i += 1
            continue

        if code == 302:
            print(f"Testing Payload {i} : Vulnerable")
            print(test_url)
        elif code == 200:
            print(f"Testing Payload {i} : Not Vulnerable")
        else:
            print(f"Testing Payload {i} : Not Vulnerable")

        i += 1
