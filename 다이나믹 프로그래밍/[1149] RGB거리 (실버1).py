# https://www.acmicpc.net/problem/1149

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]

for i in range(N):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))