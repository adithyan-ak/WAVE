
from requests import get


def ReverseIP(host, port):
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        print(result)
    except:
        print('Invalid IP address')

