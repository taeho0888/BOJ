# https://www.acmicpc.net/problem/15683

import sys
from itertools import permutations, product
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
# checked = [[False]*M for _ in range(N)]
camera = []
wall = 0
for n in range(N):
    for m in range(M):
        if 0 < room[n][m] < 6:
            camera.append((n, m, room[n][m]))
        elif room[n][m] == 6:
            wall += 1
        
# 오른: (0, 1)
# 아래: (1, 0)
# 왼쪽: (0, -1)
# 위쪽: (-1, 0)
CCTV = {
    1: [
        [(0, 1)], 
        [(1, 0)],
        [(0, -1)], 
        [(-1, 0)]
    ],
    2: [
        [(0, 1), (0, -1)],
        [(1, 0), (-1, 0)]
    ],
    3: [
        [(-1, 0), (0, 1)],
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)]
    ],
    4: [
        [(0, -1), (-1, 0), (0, 1)],
        [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)],
        [(1, 0), (0, -1), (-1, 0)]
    ],
    5: [
        [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ]
}

def bfs(product_list, checked):
    for i, j, d, c in product_list:
        q = deque([])
        checked[i][j] = True
        for dx, dy in CCTV[d][c]:
            q.append((i, j))

            while q:
                x, y = q.popleft()
                nx, ny = x + dx, y + dy
                if (0 <= nx < N) and (0 <= ny < M) and (room[nx][ny] != 6):
                    checked[nx][ny] = True
                    q.append((nx, ny))

    count = 0
    for n in range(N):
        for m in range(M):
            if not checked[n][m]:
                count += 1
    return count - wall

case = []
for x, y, d in camera:
    cur_case = []
    for __ in range(len(CCTV[d])):
        cur_case.append((x, y, d, __))
    case.append(cur_case)

answer = float('inf')
for pdt in product(*case):
    answer = min(answer, bfs(list(pdt), [[False]*M for _ in range(N)]))

print(answer)