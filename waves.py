import socket
from Plugins.reverseip import ReverseIP
from Plugins.subdomain import SubDomain
from Plugins.nslookup import nsLookup
from Plugins.cmsdetect import CMSdetect
from Plugins.nmap_recon import DefaultPort,Customrange
from Vulnerabilities.clickjacking import ClickJacking
from Vulnerabilities.hostheader import HostHeader
from Vulnerabilities.cors import Cors
from Vulnerabilities.openredirect import OpenRedirect
from Vulnerabilities.bruteforce import ssh,ftp
def Banner():
    print('''
dP   dP   dP  .d888888  dP     dP  88888888b 
88   88   88 d8'    88  88     88  88        
88  .8P  .8P 88aaaaa88a 88    .8P a88aaaa    
88  d8'  d8' 88     88  88    d8'  88        
88.d8P8.d8P  88     88  88  .d8P   88        
8888' Y88'   88     88  888888'    88888888P \n''')

host = None
port = None


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
    Banner()
    global host
    host = input("Enter the Target Host : ")
    global port
    port = int(input("Enter the Target port : "))
    print('')
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

NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}

def nmaprec(host,port):

    Choice = 1
    while True:
        print("1. Scan Default Ports (22-443)")
        print("2. Enter Custom Range")
        print("3. Back to Main Menu")
        print('')
        Choice = int(input(">> "))
        if (Choice >= 0) and (Choice < 3):
            NmapFunctions[Choice](host, port)
        elif Choice == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")

BruteFunctions = {
        1: ssh,
        2: ftp
    }

def BruteForce(host, port):
    Selection = 1
    while True:
        print('')
        print("1. SSH")
        print("2. FTP")
        print("3. Main Menu")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection >= 0) and (Selection < 3):
            BruteFunctions[Selection](host, port)
        elif Selection == 3:
            Menu()
        else:
            print("Please choose an Appropriate option")



MainFunctions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: ClickJacking,
 5: OpenRedirect,
 6: Cors,
 7: HostHeader,
 8: CMSdetect,
 9: nmaprec,
10: BruteForce
}

def Menu():
    Selection = 1
    while True:
        print('')
        print("1. ReverseIP")
        print("2. SubDomain")
        print("3. nsLookup")
        print("4. ClickJacking")
        print("5. OpenRedirect")
        print("6. CORS")
        print("7. Host Header Injection")
        print('8. CMS Detection')
        print("9. Nmap Port Scan")
        print("10. BruteForce")
        print("11. Exit")
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection >= 0) and (Selection < 11):
            MainFunctions[Selection](host, port)
        elif Selection == 11:
            exit()
        else:
            print("Please choose an Appropriate option")



#calling main methods
if __name__ == "__main__":
    Main()
    Menu()