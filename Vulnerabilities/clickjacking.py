from urllib.request import urlopen
from urllib.parse import urlparse, urlunparse

# Define whitelist of allowed hosts and ports
ALLOWED_HOSTS = {"example.com", "www.example.com"}
ALLOWED_PORTS = {80, 443}


def ClickJacking(host, port):
    # Validate host against whitelist
    if host not in ALLOWED_HOSTS:
        print("Host is not allowed")
        return

    # Validate port against whitelist
    if port not in ALLOWED_PORTS:
        print("Port is not allowed")
        return

    # Determine scheme based on port
    if port == 80:
        scheme = 'http'
    elif port == 443:
        scheme = 'https'
    else:
        # Should not reach here due to whitelist, but keep for safety
        print("Couldn't fetch data for the given PORT")
        return

    # Construct URL in a safe manner
    netloc = host
    # Append port to netloc if not default port for scheme
    if (scheme == 'http' and port != 80) or (scheme == 'https' and port != 443):
        netloc = f"{host}:{port}"

    # Build complete URL
    url = urlunparse((scheme, netloc, '', '', '', ''))

    # Further parse and validate URL
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https') or not parsed_url.netloc:
        print("Invalid URL constructed")
        return

    # Additional check to prevent embedded credentials or path in host
    if '@' in parsed_url.netloc or '/' in parsed_url.netloc:
        print("Invalid characters in host")
        return

    try:
        data = urlopen(url)
        headers = data.info()
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    if "X-Frame-Options" not in headers:
        print("Website is vulnerable to ClickJacking")
    else:
        print("Website is not Vulnerable to ClickJacking")
