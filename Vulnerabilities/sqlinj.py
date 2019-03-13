import requests



payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
    for payload in payloads:
        website = domain + "?" + ("&".join([param + payload for param in queries]))
        source = web.gethtml(website)
        if source:
            vulnerable, db = sqlerrors.check(source)
            if vulnerable and db != None:
                std.showsign(" vulnerable")
                return True, db