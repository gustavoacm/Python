import re

def fun(s):
    if s.count('@') == 1:
        username = s[0:s.find('@')]
        ns = s.replace(username+'@','')
        if ns.count('.') == 1:
            website = ns[0:ns.find('.')]
            extension = ns.replace(website+'.','')
            patron_un = r'^[A-Za-z0-9_-]+$'
            patron_ws = r'^[A-Za-z0-9]+$'
            patron_ext = r'^[A-Za-z]+$'
            if re.fullmatch(patron_un, username):
                if re.fullmatch(patron_ws, website):
                    if re.fullmatch(patron_ext, extension) and len(extension) <= 3:
                        return True
        else:
            return False
    else:
        return False
    return False
 
 
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)