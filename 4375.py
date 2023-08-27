def check_all_one(n):
    remainder = 0
    for i in range(1, n + 1):
        remainder = (remainder * 10 + 1) % n
        if remainder == 0:
            return i


while True:
    try:
        n = int(input())
        if n == 2 or n == 5:
            continue
        print(check_all_one(n))
    except EOFError:
        break
