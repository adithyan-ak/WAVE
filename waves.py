import socket
from Plugins.reverseip import ReverseIP
from Plugins.subdomain import SubDomain
from Plugins.nslookup import nsLookup
from Vulnerabilities.clickjacking import ClickJacking
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




# Dicitionary mapping to call methods
def choice(i, host):
    front = {
        1: lambda: ReverseIP(host),
        2: lambda: SubDomain(host),
        3: lambda: nsLookup(host),
        4: lambda: ClickJacking(host,port),
        5: lambda: OpenRedirect(host,port),
        6: lambda: Exit(),
    }
    print(front.get(i, lambda: 'Invalid')())

def Exit():
    exit()

# Displaying the choice
def Menu():
    print('''
    1. Reverse IP Lookup
    2. SubDomain Scannner
    3. NSlookup 
    4. ClickJacking
    5. OpenRedirect
    6. Exit\n''')
    option = int(input("Enter your choice :"))
    choice(option, host)


#calling main methods
Main()
while True:
    Menu()







