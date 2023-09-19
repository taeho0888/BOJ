# https://www.acmicpc.net/problem/14501

import sys
input = sys.stdin.readline

n = int(input())
T, P = [], []
dp = [0] * (n + 1)

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(n-1, -1, -1):
    if i + T[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])
