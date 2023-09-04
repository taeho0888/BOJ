# https://www.acmicpc.net/problem/14502

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
infect_root = [[0]*M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(visited, x, y, root):
    if lab[x][y] == 2:
        return root

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and (lab[nx][ny] == 0):
            visited[nx][ny] = True
            root.append((nx, ny))
            dfs(visited, nx, ny, root)


for n in range(N):
    for m in range(M):
        if lab[n][m] == 1:
            visited = [[False]*M for _ in range(N)]
            root = [(n, m)]
            infected = dfs(visited, n, m, root)
            print(infected)


print(infect_root)
