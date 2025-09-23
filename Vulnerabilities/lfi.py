import requests
import re
import socket

ALLOWED_DOMAINS = {"example.com", "testsite.org", "mydomain.net"}  # Whitelist of allowed domains


def is_private_ip(ip):
    try:
        ip_addr = socket.inet_aton(ip)
        first_octet = ip.split('.')[0]
        second_octet = ip.split('.')[1]

        # 10.0.0.0/8
        if first_octet == '10':
            return True

        # 172.16.0.0/12
        if first_octet == '172' and 16 <= int(second_octet) <= 31:
            return True

        # 192.168.0.0/16
        if first_octet == '192' and second_octet == '168':
            return True

        # 127.0.0.0/8 (localhost)
        if first_octet == '127':
            return True

        # 169.254.0.0/16 (link-local)
        if first_octet == '169' and second_octet == '254':
            return True

        return False
    except Exception:
        return False


def Lfi(domain, port):
    # Validate domain format
    domain_pattern = re.compile(r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$')
    ip_pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}$')

    if not (domain_pattern.match(domain) or ip_pattern.match(domain)):
        raise ValueError("Invalid domain format")

    # If domain is IP, check if it is private
    if ip_pattern.match(domain):
        if is_private_ip(domain):
            raise ValueError("Private IP addresses are not allowed")

    # If domain is not IP, check whitelist
    else:
        if domain not in ALLOWED_DOMAINS:
            raise ValueError("Domain not allowed")

    payload = {'key': '1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66', 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    return response
