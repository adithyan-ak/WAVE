
import socket


def nsLookup(host, port):
    # Validate that host is a valid hostname or IP address
    try:
        # Attempt to resolve the host locally
        socket.gethostbyname(host)
    except socket.error:
        print("Invalid or unresolvable host provided.")
        return

    # Proceed with DNS lookup using local system resolver
    try:
        # Using socket.getaddrinfo as a safe alternative to external HTTP DNS lookup
        addr_info = socket.getaddrinfo(host, port)
        for info in addr_info:
            print(f"Address info: {info}")
    except Exception as e:
        print(f"Error resolving host: {e}")


host = 'www.skcet.ac.in'
