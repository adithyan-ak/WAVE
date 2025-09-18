
import socket


def nsLookup(host, port):
    # Validate host: allow only valid domain names or IP addresses
    try:
        # Attempt to resolve the host locally to prevent SSRF
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Invalid host provided.")
        return

    # Optional: Implement a whitelist of allowed domains or IPs
    allowed_domains = ["skcet.ac.in"]
    if not any(host.endswith(domain) for domain in allowed_domains):
        print("Host not in allowed domains whitelist.")
        return

    # Perform local DNS lookup to avoid SSRF
    try:
        # Get all DNS records (A records) for the host
        # Using socket.gethostbyname_ex to get all associated IPs
        hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(host)
        print(f"DNS Lookup results for {host}:")
        for ipaddr in ipaddrlist:
            print(ipaddr)
    except Exception as e:
        print(f"Error during DNS lookup: {e}")


host = 'www.skcet.ac.in'

