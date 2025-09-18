
import json
import re
import requests



    # Validate the 'host' to ensure it is a valid domain name
    # Regex pattern for domain validation (basic check)
    domain_pattern = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)'
        r'(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?$'
    )

    if not domain_pattern.match(host):
        raise ValueError("Invalid domain name provided")
def SubDomain(host, port):

    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    subdomains = response.json()
    for x in subdomains.get('domain_siblings', []):
    for x in subdomains['domain_siblings']: