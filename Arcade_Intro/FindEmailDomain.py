def findEmailDomain(address):
    s = address.split('@')
    return s[len(s)-1]
