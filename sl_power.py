# x 的　Ｎ　次方
def power(x, n=2):
    # 5**2, 5 ** 0
    s = 1
    for i in range(0, n):
        s *= x
    return s


if __name__ == "__main__":
    print(power(2, 5))
    print(power(2))
