import re

def email_parse(email):
    match = re.findall(r'([1-9A-Za-z]+)@([a-z]+[.][a-z]+)', email)
    if match:
        return {'username': match[0][0], 'domain': match[0][1]}
    else:
        msg = f'Wrong email:{email}'
        raise ValueError(msg)

print(email_parse('omarov2222@google.com'))
