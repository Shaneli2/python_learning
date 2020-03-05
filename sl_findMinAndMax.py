def findMinAndMax(L=None):
    # L=[1,2,3,5,7]
    if L == [] or L is None:
        return None, None

    min_value = L[0]
    max_value = L[0]
    for i in L:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    return min_value, max_value


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
