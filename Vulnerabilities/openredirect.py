from urllib.request import *
from urllib.parse import urlparse


def OpenRedirect(host, port):
    # Define a whitelist of allowed hosts
    allowed_hosts = {"example.com", "testsite.com"}

    # Validate host is in whitelist
    if host not in allowed_hosts:
        print(f"Host '{host}' is not in the allowed hosts whitelist.")
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

    url = scheme + host
    q = Request(url)
    q.add_header('X-Forwarded-Host', 'https://google.com')

    try:
        a = urlopen(q).getcode()
    except Exception as e:
        print(f"Error fetching initial URL: {e}")
        return

    if a == 302:
        print("Testing Payload 1 : Vulnerable to X-Forwarded-Host Header")
    else:
        print('Testing Payload 1 : Not Vulnerable')

    try:
        with open("redirectpayloads.txt", "r") as f:
            f1 = f.readlines()
    except Exception as e:
        print(f"Error reading payloads file: {e}")
        return

    for x in f1:
        x = x.strip()
        if not x:
            continue

        if i >= 34:
            break

        try:
            test_url = scheme + host + x

            # Validate the constructed URL
            parsed_url = urlparse(test_url)

            # Ensure the URL scheme and netloc are correct
            if parsed_url.scheme not in ('http', 'https'):
                print(f"Testing Payload {i} : Invalid URL scheme")
                i += 1
                continue

            if parsed_url.hostname != host:
                print(f"Testing Payload {i} : URL hostname mismatch")
                i += 1
                continue

            data = urlopen(test_url)
            status_code = data.getcode()

        except Exception:
            print(f"Testing Payload {i} : Error")
            i += 1
            continue

        if status_code == 302:
            print(f"Testing Payload {i} : Vulnerable")
            print(test_url)
        elif status_code == 200:
            print(f"Testing Payload {i} : Not Vulnerable")
        else:
            print(f"Testing Payload {i} : Not Vulnerable")

        i += 1
