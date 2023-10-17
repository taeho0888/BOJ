# https://www.acmicpc.net/problem/2667
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True

            if board[i][j] == 1:
                q = deque([(i, j)])
                count = 1

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]

                        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and board[nx][ny] == 1:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            count += 1
                answer.append(count)

print(len(answer))
for home in sorted(answer):
    print(home)
