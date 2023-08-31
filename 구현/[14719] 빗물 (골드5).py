# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
wall = list(map(int, input().split()))

rain = 0

for i in range(1, W-1):
    left = max(wall[:i])
    right = max(wall[i:])
    cur_rain = min(left, right) - wall[i]
    if cur_rain > 0:
        rain += cur_rain

print(rain)
