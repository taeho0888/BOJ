# https://www.acmicpc.net/problem/14502

import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(lab):
    visited = [[False]*M for _ in range(N)]
    count = 0

    for v in range(len(virus)):
        n, m = virus[v]
        stack = [(n, m)]

        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and lab[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return safe_count - count

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]


blank_space = []
virus = []
safe_count = -3
for n in range(N):
    for m in range(M):
        if lab[n][m] == 0:
            blank_space.append((n, m))
            safe_count += 1
        elif lab[n][m] == 2:
            virus.append((n, m))

cur_max = -1
for cbn in combinations([i for i in range(len(blank_space))], 3):
    cur_lab = deepcopy(lab)
    for c in cbn:
        x, y = blank_space[c]
        cur_lab[x][y] = 1

    cur_max = max(cur_max, dfs(cur_lab))

print(cur_max)