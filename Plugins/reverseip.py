
from requests import get


def ReverseIP(host):
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
    try:
        result = get(lookup).text
        return result
    except:
        print('%s Invalid IP address' % bad)
