# https://www.acmicpc.net/problem/11047
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
for coin in coins[::-1]:
    if K == 0:
        break
    elif coin > K:
        continue
    else:
        count += K // coin
        K %= coin

print(count)