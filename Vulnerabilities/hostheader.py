from urllib.request import *


def OpenRedirect(host,port):
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")
    url = (port + host)
    q = Request(url)
    q.add_header('Host', 'https://google.com')
    a = urlopen(q).getcode()
    if a == 302:
        print("Testing Payload 1 : Vulnerable to Host Header Injection")
    else:
        print('Testing Payload 1 : Not Vulnerable')

OpenRedirect('www.skcet.ac.in',80)