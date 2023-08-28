def dp(num):
    if num == 4:
        raise TypeError
    elif num % 5 == 0:
        return num // 5
    else:
        return 1 + dp(num-3)


try:
    print(dp(int(input())))
except TypeError:
    print(-1)
