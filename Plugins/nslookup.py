
from requests import get


def nsLookup(host, port):
    result = get('http://api.hackertarget.com/dnslookup/?q=' + host).text
    print(result)

host = 'www.skcet.ac.in'

