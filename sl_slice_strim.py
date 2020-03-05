def sl_trim1(s):
    if s.isspace() or s == '':
        return ''

    while s[0] == ' ':
        s = s[-(len(s) - 1):]

    while s[len(s) - 1] == ' ':
        s = s[:len(s) - 1]
    return s


def sl_trim(s):
    while s != '' and s[:1] == ' ':
        s = s[1:]
    while s != '' and s[-1:] == ' ':
        s = s[:-1]
    return s


# testing

if __name__ == "__main__":
    if sl_trim('hello  ') != 'hello':
        print('测试失败!')
    elif sl_trim('  hello') != 'hello':
        print('测试失败!')
    elif sl_trim('  hello  ') != 'hello':
        print('测试失败!')
    elif sl_trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif sl_trim('') != '':
        print('测试失败!')
    elif sl_trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
