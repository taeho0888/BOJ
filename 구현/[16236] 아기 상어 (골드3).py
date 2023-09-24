from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_distance(sx, sy, ex, ey):
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    q = deque([(sx, sy, 0)])

    while q:
        x, y, d = q.popleft()

        if (x == ex) and (y == ey):
            return d
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and (space[nx][ny] <= baby_shark[2]):
                visited[nx][ny] = True
                q.append((nx, ny, d+1))

    return -1


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
fish = []
for n in range(N):
    for m in range(N):
        if space[n][m] == 0:
            continue
        elif 0 < space[n][m] < 7:
            fish.append((n, m, space[n][m]))
        elif space[n][m] == 9:
            baby_shark = (n, m, 2)
            space[n][m] = 0
eaten = [False]*len(fish)

time, count = 0, 0
while True:
    candidate = []
    for i in range(len(fish)):
        if not eaten[i] and (fish[i][2] < baby_shark[2]):
            sx, sy, ex, ey = baby_shark[0], baby_shark[1], fish[i][0], fish[i][1]
            dist = get_distance(sx, sy, ex, ey)
            if dist != -1:
                candidate.append((fish[i][0], fish[i][1], fish[i][2], dist))
    
    if not candidate:
        break

    sorted_candidate = sorted(candidate, key=lambda x: (x[3], x[0], x[1]))
    new_x, new_y, size, distance = sorted_candidate[0]

    for j in range(len(fish)):
        if new_x == fish[j][0] and new_y == fish[j][1]:
            eaten[j] = True
            break

    count += 1
    if count == baby_shark[2]:
        count = 0
        new_size = baby_shark[2] + 1
        baby_shark = (new_x, new_y, new_size)
    else:
        baby_shark = (new_x, new_y, baby_shark[2])

    time += distance
    # print()
    # print(f"time = {time}\ncount = {count}\nbaby shark = ({baby_shark[0]}, {baby_shark[1]})")
    # print(sorted_candidate)


print(time)