import requests
import re


header1 = None
domain2 = None
header2 = None
domain3 = None
header3 = None

# Define allowed hosts and ports whitelist
ALLOWED_HOSTS = {'example.com', 'testsite.com', 'mydomain.org'}
ALLOWED_PORTS = {80, 443}


def is_valid_hostname(hostname):
    # Basic regex for hostname validation (allowing letters, digits, hyphens, dots)
    if len(hostname) > 253:
        return False
    if hostname[-1] == ".":  # strip trailing dot
        hostname = hostname[:-1]
    allowed = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$")
    return all(allowed.match(x) for x in hostname.split("."))


def validate_host_port(host, port):
    if port not in ALLOWED_PORTS:
        print(f"Port {port} is not allowed. Allowed ports are: {ALLOWED_PORTS}")
        exit()
    if not is_valid_hostname(host):
        print(f"Host '{host}' is invalid or not allowed.")
        exit()
    if host not in ALLOWED_HOSTS:
        print(f"Host '{host}' is not in the allowed hosts list.")
        exit()


def Cors(host, port):
    validate_host_port(host, port)

    if port == 80:
        scheme = 'http://'
    elif port == 443:
        scheme = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
        exit()

    print("1. CORS check in Default Host")
    print("2. CORS check in Host's Custom Endpoint")
    print('')
    choice = int(input('>> '))
    print('')
    cookies = input("Paste the Cookies (If None,then hit enter) : ")
    global header1
    global domain2
    global header2
    global domain3
    global header3
    if cookies == '':

        header1 = {'Origin': 'http://evil.com'}

        domain2 = host + '.evil.com'

        header2 = {'Origin': scheme + domain2}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': scheme + domain3}

        Choices(host, scheme, choice)
    else:

        header1 = {'Origin': 'http://evil.com', 'Cookie': cookies}

        domain2 = host + '.evil.com'

        header2 = {'Origin': scheme + domain2, 'Cookie': cookies}

        domain3 = host + '%60cdl.evil.com'

        header3 = {'Origin': scheme + domain3, 'Cookie': cookies}

        Choices(host, scheme, choice)


def Choices(host, scheme, choice):
    if choice == 2:
        endpoint = input("Enter the Custom Endpoint : ")
        # Validate the custom endpoint
        if not is_valid_hostname(endpoint):
            print(f"Custom endpoint '{endpoint}' is invalid.")
            exit()
        if endpoint not in ALLOWED_HOSTS:
            print(f"Custom endpoint '{endpoint}' is not in the allowed hosts list.")
            exit()
        host = endpoint
        WrongChoice(host, scheme)

    elif choice == 1:
        print("Checking Default Host ")
        url = (scheme + host)
        print("Testing with Payload %s" % header1)
        response = requests.get(url, headers=header1)
        if 'evil.com' in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header2)
        response = requests.get(url, headers=header2)

        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')

        print("Testing with Payload %s" % header3)
        response = requests.get(url, headers=header3)
        if domain2 in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print('')
    else:
        print("Wrong Choice")
        print("Checking Default Host")
        WrongChoice(host, scheme)


def WrongChoice(host, scheme):
    url = (scheme + host)
    print("Testing with Payload %s" % header1)
    response = requests.get(url, headers=header1)
    if 'evil.com' in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header2)
    response = requests.get(url, headers=header2)

    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')

    print("Testing with Payload %s" % header3)
    response = requests.get(url, headers=header3)
    if domain2 in response.headers:
        print("Vulnerable to Cross Origin Resource Sharing")
    else:
        print("Not Vulnerable to Cross Origin Resource Sharing")
    print('')
