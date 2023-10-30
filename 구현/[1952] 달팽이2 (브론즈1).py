# https://www.acmicpc.net/problem/1952

m, n = map(int, input().split())
visited = [[0]*n for _ in range(m)]
count, i = 0, 0
MAX_COUNT = m*n
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
visited[0][0] = 1

while count < MAX_COUNT:
    nx, ny = x + dx[i % 4], y + dy[i % 4]

    # 같은 방향으로 진행 불가하면
    if (0 > nx) or (nx >= m) or (0 > ny) or (ny >= n) or visited[nx][ny]:
        # 한번 꺾어
        cx, cy = x + dx[(i+1) % 4], y + dy[(i+1) % 4]
        # 꺾었는데 진행 되면 ok
        if (0 <= cx < m) and (0 <= cy < n) and not visited[cx][cy]:
            i += 1
            nx, ny = cx, cy
        else:
            break

    # 같은 방향으로 진행 가능하면
    x, y = nx, ny
    visited[x][y] = 1
    count += 1
    # print()
    # for row in visited:
    #     print(*row)

print(i)
