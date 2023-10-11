# https://www.acmicpc.net/problem/2573
from collections import deque
from copy import deepcopy


def count_land(board, iceberg):
    land = 0
    visited = [[False]*m for _ in range(n)]
    for x, y in iceberg:  # 빙산 위치만 확인
        if not visited[x][y]:
            visited[x][y] = True
            land += 1
            q = deque([(x, y)])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny] and board[nx][ny] != 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    return land


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
iceberg = {(i, j) for i in range(n) for j in range(m) if board[i][j] != 0}

year = 0
while True:
    if count_land(board, iceberg) > 1:
        break

    if not iceberg:
        print(0)
        exit()

    melt_dict = {}
    for x, y in iceberg:
        melt = sum(1 for k in range(4) if 0 <= x +
                   dx[k] < n and 0 <= y + dy[k] < m and board[x + dx[k]][y + dy[k]] == 0)
        melt_dict[(x, y)] = melt

    new_iceberg = set()
    for (x, y), melt in melt_dict.items():
        board[x][y] = max(board[x][y] - melt, 0)
        if board[x][y] > 0:
            new_iceberg.add((x, y))
    iceberg = new_iceberg
    year += 1

print(year)
