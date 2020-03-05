import re


def is_valid_email(addr):
    re_mailaddr = re.compile(r'\<?\w*\s?\w*\>?\s?\.?\#?\w*\@\w*\.[com]|[org]')
    if re_mailaddr.match(addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('<Tom Paris> tom@voyager.org')

assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    re_mailaddr = re.compile(r'\<?(\w*\s?\w*)\>?\s?\.?\#?\w*\@\w*\.org')
    if re_mailaddr.match(addr):
        return re_mailaddr.match(addr).group(1)
    else:
        return None


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok2')