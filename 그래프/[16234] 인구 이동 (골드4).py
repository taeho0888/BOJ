# https://www.acmicpc.net/problem/16234
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
day = 0

while True:
    # 국경이 열리는 지 체크
    union_list = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                cur_union = [(i, j)]
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        
                        if 0 > nx or N <= nx or 0 > ny or N <= ny:
                            continue
                        
                        # 인구차이
                        pop_dif = abs(country[x][y] - country[nx][ny])
                        if not visited[nx][ny] and (L <= pop_dif <= R):
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cur_union.append((nx, ny))
                if len(cur_union) > 1:
                    union_list.append(cur_union)

    # 안열린다면 break
    if not union_list:
        break

    # 연합끼리 인구 이동
    for union in union_list:
        pop_sum = 0
        for x, y in union:
            pop_sum += country[x][y]
        population = pop_sum // len(union)

        for x, y in union:
            country[x][y] = population
    
    # for row in country:
    #     print(row)

    # 날짜 하루 늘림
    day += 1

print(day)