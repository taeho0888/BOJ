# https://www.acmicpc.net/problem/2206
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, d, w):
    global answer

    if w == 2:
        return

    if x == n-1 and y == m-1:
        answer = min(answer, d)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, d+1, w+board[nx][ny])
            visited[nx][ny] = False


n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*m for _ in range(n)]
visited[0][0] = True
answer = float('inf')
dfs(0, 0, 1, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
