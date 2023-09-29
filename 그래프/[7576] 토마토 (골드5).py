# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

q = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j, 0))
            box[i][j] = 0
            visited[i][j] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, t = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and (box[nx][ny] == 0):
            visited[nx][ny] = True
            box[nx][ny] = t+1
            q.append((nx, ny, t+1))

day = -1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and (box[i][j] == 0):
            print(-1)
            exit()
        day = max(day, box[i][j])

print(day)