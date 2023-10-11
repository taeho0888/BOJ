# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
input = sys.stdin.readline

# 오, 아래, 왼, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
di = 0

n = int(input())
k = int(input())
apples = [[0]*n for _ in range(n)]
for _ in range(k):
    ax, ay = map(int, input().split())
    apples[ax-1][ay-1] = 1
moves = deque([input().split() for _ in range(int(input()))])

snake = deque([(0, 0)])
visited = [[0]*n for _ in range(n)]
visited[0][0] = 1
time = 0
sx, sy = 0, 0
next_dir_change_time, c = moves.popleft()

while True:
    # 시간 늘리고 한칸 이동
    time += 1
    nx, ny = sx + dx[di], sy + dy[di]

    # 탈출 조건
    if (0 > nx) or (nx >= n) or (0 > ny) or (ny >= n) or visited[nx][ny]:
        break

    # 유효하다면 뱀 큐에 추가
    visited[nx][ny] = 1
    snake.append((nx, ny))
    sx, sy = nx, ny

    # 사과가 있는 자리라면 꼬리 회수 X, 없으면 회수
    if apples[sx][sy] == 1:
        apples[sx][sy] = 0
    else:
        cx, cy = snake.popleft()
        visited[cx][cy] = 0

    # 방향 돌릴 타임이 되면 방향 돌림
    if time == int(next_dir_change_time):
        if c == "D":
            di = (di+1) % 4
        else:
            di = (di-1) % 4

        # 다음 움직임이 있다면 업데이트, 없다면 놔둠
        if moves:
            next_dir_change_time, c = moves.popleft()

print(time)
