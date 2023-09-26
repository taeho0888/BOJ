# https://school.programmers.co.kr/learn/courses/30/parts/12421

def dfs(board, visited, i, j, target):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n = len(board)
    visited[i][j] = True
    stack = [(i, j)]
    block = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and (board[nx][ny] == target):
                visited[nx][ny] = True
                stack.append((nx, ny))
                block.append((nx, ny))
    
    return block, visited


def tilt(square):
    n, m = len(square), len(square[0])
    new_square = []
    for i in range(m):
        cur_row = []
        for j in range(n-1, -1, -1):
            cur_row.append(square[j][i])
        new_square.append(cur_row)

    return new_square


def is_fit(blank, block):
    # 갯수 다르면 맞지 않음
    if len(blank) != len(block):
        return False
    
    # blank를 정사각형 안에 넣기
    max_x, min_x = max([x[0] for x in blank]), min([x[0] for x in blank])
    max_y, min_y = max([x[1] for x in blank]), min([x[1] for x in blank])
    h, w = max_x - min_x + 1, max_y - min_y + 1

    blank_square = [[0]*w for _ in range(h)]
    for i, b in enumerate(blank):
        blank_square[b[0] - min_x][b[1] - min_y] = 1

    # block을 정사각형 안에 넣기
    max_x, min_x = max([x[0] for x in block]), min([x[0] for x in block])
    max_y, min_y = max([x[1] for x in block]), min([x[1] for x in block])
    h, w = max_x - min_x + 1, max_y - min_y + 1
    
    block_square = [[0]*w for _ in range(h)]
    for i, b in enumerate(block):
        block_square[b[0] - min_x][b[1] - min_y] = 1

    # 4방향 다 돌렸을 때 맞으면 return true
    for _ in range(4):
        if blank_square == block_square:
            return True
        block_square = tilt(block_square)
    
    return False


def solution(game_board, table):
    n = len(game_board)
    
    # board에서 빈칸 파악
    blank = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if game_board[i][j] == 0:
                    b, visited = dfs(game_board, visited, i, j, 0)
                    blank.append(b)
              
    # table에서 빈칸 파악
    block = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if table[i][j] == 1:
                    b, visited = dfs(table, visited, i, j, 1)
                    block.append(b)

    # 빈칸이랑 동일한 블록 있는 지 파악 -> 있으면 빈칸 갯수 더하기
    answer = 0
    empty, used = [True]*len(blank), [False]*len(block)
    for i in range(len(blank)):
        for j in range(len(block)):
            if empty[i] and not used[j] and is_fit(blank[i], block[j]):
                empty[i], used[j] = False, True
                answer += len(block[j])
                
    return answer