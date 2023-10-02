# https://www.acmicpc.net/problem/3055
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

water = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            dochi = (i, j)
        elif board[i][j] == 'D':
            bieber = (i, j)
        elif board[i][j] == '*':
            water.append((i, j))

visited = [[False]*C for _ in range(R)]
visited[dochi[0]][dochi[1]] = True

q = deque([(dochi, 0)])

def spread_water():
    new_water = []
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.':
                board[nx][ny] = '*'
                new_water.append((nx, ny))
    return new_water

answer = "KAKTUS"
while q:
    water = spread_water()
    length = len(q)
    for _ in range(length):
        (x, y), time = q.popleft()

        if (x, y) == bieber:
            answer = time
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < R) and (0 <= ny < C) and not visited[nx][ny]:
                if board[nx][ny] in ['.', 'D']:
                    visited[nx][ny] = True
                    q.append(((nx, ny), time + 1))

print(answer)
