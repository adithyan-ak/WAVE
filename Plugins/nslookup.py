
from requests import get


def nsLookup(host):
    result = get('http://api.hackertarget.com/dnslookup/?q=' + host).text
    return result

host = 'www.skcet.ac.in'

nsLookup(host)