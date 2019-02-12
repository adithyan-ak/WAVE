from urllib.request import *


def OpenRedirect(host,port):
    if port == 80:
        port = 'http://'
    elif port == 443:
        port = 'https://'
    else:
        print("Could'nt fetch data for the given PORT")

    print('Testing with all available payloads')

    i = 2



    url = (port + host)
    q = Request(url)
    q.add_header('X-Forwarded-Host', 'https://google.com')
    a = urlopen(q).getcode()
    if a == 302:
        print("Testing Payload 1 : Vulnerable to X-Forwarded-Host Header")
    else:
        print('Testing Payload 1 : Not Vulnerable')

    f = open("redirectpayloads.txt", "r")
    f1 = f.readlines()

    for x in f1:

        while i < 34:

             try:

                 url = (port + host + x)
                 data = urlopen(url)
                 x = data.getcode()

             except:
                 print("Testing Payload %i : Error" % i)
                 break


             if x == 302:
                 print("Testing Payload %i : Vulnerable" % i)
                 print(url)
                 break

             elif x == 200:
                 print("Testing Payload %i : Not Vulnerable" % i)
                 break

             else:
                 print("Testing Payload %i : Not Vulnerbale" % i)
                 break

        i+=1



OpenRedirect('www.skcet.ac.in',80)