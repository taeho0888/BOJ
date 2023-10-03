# https://www.acmicpc.net/problem/17144
def print_board():
    print()
    for i in range(R):
        for j in range(C):
            print(f"{board[i][j]:3d}", end="")
        print()

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        up_cleaner, down_cleaner = i, i+1
        break

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# print_board()

for _ in range(T):
    # 먼지 계산
    dust = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 4:
                dust.append((i, j, board[i][j]))

    # 먼지 확산
    for (x, y, d) in dust:
        spread_num = 0
        spread_dust = d // 5
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (0 <= nx < R) and (0 <= ny < C) and board[nx][ny] != -1:
                spread_num += 1
                board[nx][ny] += spread_dust
        board[x][y] -= spread_dust*spread_num

    # print_board()
    # 윗 공기정청기 작동
    board[up_cleaner-1][0] = 0
    for i in range(up_cleaner-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(up_cleaner):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[up_cleaner][i] = board[up_cleaner][i-1]
    board[up_cleaner][1] = 0

    # 아랫 공기정청기 작동
    board[down_cleaner+1][0] = 0
    for i in range(down_cleaner+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[-1][i] = board[-1][i+1]
    for i in range(R-1, down_cleaner, -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[down_cleaner][i] = board[down_cleaner][i-1]
    board[down_cleaner][1] = 0

    # print_board()

# 먼지 합 구함
answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]
print(answer)

