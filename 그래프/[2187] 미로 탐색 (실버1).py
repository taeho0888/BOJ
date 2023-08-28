# https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())
mirro = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    visited = [[False]*M for _ in range(N)]
    q = deque([(i, j, 1)])
    visited[i][j] = True

    while q:
        x, y, w = q.popleft()

        if (x, y) == (N-1, M-1):
            return w
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and mirro[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, w+1))

print(bfs(0, 0))