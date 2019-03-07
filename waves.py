import socket
from Plugins.reverseip import ReverseIP
from Plugins.subdomain import SubDomain
from Plugins.nslookup import nsLookup
from Plugins.cmsdetect import CMSdetect
from Plugins.nmap_recon import Nmap_Recon
from Vulnerabilities.clickjacking import ClickJacking
from Vulnerabilities.hostheader import HostHeader
from Vulnerabilities.cors import Cors
from Vulnerabilities.openredirect import OpenRedirect
def Banner():
    print('''
    '##:::::'##::::'###::::'##::::'##:'########::'######::
     ##:'##: ##:::'## ##::: ##:::: ##: ##.....::'##... ##:
     ##: ##: ##::'##:. ##:: ##:::: ##: ##::::::: ##:::..::
     ##: ##: ##:'##:::. ##: ##:::: ##: ######:::. ######::
     ##: ##: ##: #########:. ##:: ##:: ##...:::::..... ##: 
     ##: ##: ##: ##.... ##::. ## ##::: ##:::::::'##::: ##:
    . ###. ###:: ##:::: ##:::. ###:::: ########:. ######::
    :...::...:::..:::::..:::::...:::::........:::......::: \n''')

Banner()

host = input("Enter the Target Host : ")
port = int(input("Enter the Target port : "))
print('\n')

# Checking whether the target host is alive or dead
def CheckTarget():

    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def Main():
    print("Starting WAVES \n")
    print("Checking whether the Target is reachable \n")
    # calling CheckTarget method
    if CheckTarget()==True:
        print("Target Alive \n")
        print("Host : " + host)
        print("Port : %s" % port)
    else:
        print("The Host is Unreachable \n")
        exit()

#calling main methods
Main()

Functions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: ClickJacking,
 5: OpenRedirect,
 6: Cors,
 7: HostHeader,
 8: CMSdetect,
 9: Nmap_Recon
}

Selection = 1
while True:
    print('\n')
    print("1. ReverseIP")
    print("2. SubDomain")
    print("3. nsLookup")
    print("4. ClickJacking")
    print("5. OpenRedirect")
    print("6. CORS")
    print("7. Host Header Injection")
    print('8. CMS Detection')
    print("9. Nmap Port Scan")
    print("10. Quit")
    print('\n')
    Selection = int(input("Choose an option: "))
    print('\n')
    if (Selection >= 0) and (Selection < 10):
        Functions[Selection](host, port)
    elif Selection == 10:
        exit()
    else:
        print("Please choose an Appropriate option")


