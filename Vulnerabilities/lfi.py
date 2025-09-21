import requests
import re

def Lfi(domain, port):
    # Validate domain to allow only valid domain names or IP addresses
    domain_pattern = re.compile(r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$')
    ip_pattern = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}$')
    if not (domain_pattern.match(domain) or ip_pattern.match(domain)):
        raise ValueError("Invalid domain format")

    payload = {'key': '1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66', 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    return response
