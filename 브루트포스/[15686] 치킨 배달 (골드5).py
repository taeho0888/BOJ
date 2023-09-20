# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
input = sys.stdin.readline

# 거리 구하는 함수
def get_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

# 입력 받기
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨 리스트 구하기
house, chicken = [], []
for n in range(N):
    for m in range(N):
        if city[n][m] == 1:
            house.append((n, m))
        elif city[n][m] == 2:
            chicken.append((n, m))

# 집 별로 치킨거리 모두 구하기 / 행: 집, 열: 치킨집
chicken_distance = [[0]*(len(chicken)) for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(chicken)):
        chicken_distance[i][j] = get_distance(house[i], chicken[j])

# 치킨집에 대한 조합 생성한 뒤, 치킨 거리의 최소값 구하기
min_chicken_distance = float('inf')
for selected_chickens in combinations(range(len(chicken)), M):
    cur_chicken_distance = 0
    for i in range(len(house)):
        cur_chicken_distance += min([chicken_distance[i][j] for j in selected_chickens])
    min_chicken_distance = min(min_chicken_distance, cur_chicken_distance)

print(min_chicken_distance)