# https://www.acmicpc.net/problem/20057
import sys
inpnut = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 위, 왼, 아래, 오
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 토네이도
tornado = {
    0: {  # 위
        (0, 1): 7,
        (0, -1): 7,
        (0, 2): 2,
        (0, -2): 2,
        (-1, 1): 10,
        (-1, -1): 10,
        (-2, 0): 5,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 0): "a"
    },
    1: {  # 왼
        (-1, 0): 7,
        (1, 0): 7,
        (-1, -1): 10,
        (1, -1): 10,
        (0, -2): 5,
        (1, 1): 1,
        (-1, 1): 1,
        (2, 0): 2,
        (-2, 0): 2,
        (0, -1): "a"
    },
    2: {  # 아래
        (0, 1): 7,
        (0, -1): 7,
        (-1, -1): 1,
        (-1, -1): 1,
        (0, 2): 2,
        (0, -2): 2,
        (1, 1): 10,
        (1, -1): 10,
        (2, 0): 5,
        (1, 0): "a"
    },
    3: {  # 오
        (-1, 0): 7,
        (1, 0): 7,
        (-1, 1): 10,
        (1, 1): 10,
        (0, 2): 5,
        (1, -1): 1,
        (-1, -1): 1,
        (2, 0): 2,
        (-2, 0): 2,
        (0, 1): "a"
    }
}
# 토네이도 이동 로직
now, time, i = (int((n-1)*0.5), int((n-1)*0.5)), 0, 0
visited = [[0]*n for _ in range(n)]
visited[int((n-1)*0.5)][int((n-1)*0.5)] = 1
answer = 0

while now != (0, 0):
    time += 1
    x, y = now
    # 다음 방향으로 갈 수 있는 지 판단
    nx, ny = x+dx[(i+1) % 4], y+dy[(i+1) % 4]
    if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
        visited[nx][ny] = 1
        i = (i+1) % 4
        now = (nx, ny)
    else:
        nx, ny = x+dx[i], y+dy[i]
        visited[nx][ny] = 1
        now = (nx, ny)

    # 모래 움직임 로직
    cur_sand = board[nx][ny]
    board[nx][ny] = 0
    moved_sand = {
        1: int(cur_sand*0.01),
        2: int(cur_sand*0.02),
        5: int(cur_sand*0.05),
        7: int(cur_sand*0.07),
        10: int(cur_sand*0.1),
        "a": 0
    }
    moved_sand["a"] = cur_sand - moved_sand[1]*2 - moved_sand[2]*2 - \
        moved_sand[5] - moved_sand[7]*2 - moved_sand[10]*2
    for cur_dx_dy, per in tornado[i].items():
        cdx, cdy = cur_dx_dy
        cnx, cny = nx+cdx, ny+cdy

        if (0 <= cnx < n) and (0 <= cny < n):
            board[cnx][cny] += moved_sand[per]
        else:
            answer += moved_sand[per]

print(answer)
