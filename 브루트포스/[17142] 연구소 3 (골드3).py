# https://www.acmicpc.net/problem/17142
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

virus, blank = [], 0
for i in range(n):
    for j in range(n):
        if lab[i][j] == 0:
            blank += 1
        elif lab[i][j] == 2:
            virus.append((i, j))
            lab[i][j] = "*"

answer = float('inf')
for selected in combinations([i for i in range(len(virus))], m):
    count = 0
    visited = [[False]*n for _ in range(n)]
    q = deque([])

    for id in selected:
        x, y = virus[id]
        q.append((x, y, 0))
        visited[x][y] = True

    while q:
        x, y, t = q.popleft()

        if t > answer:
            break

        if count == blank:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and lab[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny, t+1))
                if lab[nx][ny] == 0:
                    count += 1
                    if count == blank:
                        break

    if count == blank:
        answer = min(answer, t)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
