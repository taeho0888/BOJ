# https://www.acmicpc.net/problem/7569
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0]
dz = [0, 0, 0, 1, 0, -1]

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)]
          for _ in range(h)]

good = deque([])
bad = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                good.append((i, j, k, 0))
            elif tomato[i][j][k] == 0:
                bad += 1

be_good = 0
while good:
    x, y, z, t = good.popleft()

    for l in range(6):
        nx, ny, nz = x + dx[l], y + dy[l], z + dz[l]

        if (0 <= nx < h) and (0 <= ny < n) and (0 <= nz < m) and tomato[nx][ny][nz] == 0:
            good.append((nx, ny, nz, t+1))
            tomato[nx][ny][nz] = 1
            be_good += 1

if be_good == bad:
    print(t)
else:
    print(-1)
