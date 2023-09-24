# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline

def is_possible(road):
    # 높이 차이가 있는 그룹으로 나눔
    parent = [i for i in range(N)]
    for i in range(1, N):
        if road[i-1] == road[i]:
            parent[i] = parent[i-1]

    sub_group = [[] for _ in range(N)]
    for i in range(N):
        sub_group[parent[i]].append(i)
    group = [sub for sub in sub_group if len(sub) > 0]
    len_group = len(group)

    if len_group == 1:
        return True

    height, length = [0]*len_group, [0]*len_group
    for i in range(len_group):
        length[i] = len(group[i])
        height[i] = road[group[i][0]]

    # 그룹이 2개일 경우
    if len_group == 2:
        if abs(height[0] - height[1]) > 1:
            return False
        if height[0] < height[1]:
            if length[0] < L:
                return False
        else:
            if length[1] < L:
                return False

    # 그룹이 3개 이상일 경우     
    # 높이 차이가 1초과인 그룹이 하나라도 있으면 return false
    for i in range(len_group-1):
        if abs(height[i] - height[i+1]) > 1:
            return False
        
    # 높낮높이면서 낮의 길이가 2*L이 안되면 return false
    for i in range(1, len_group-1):
        if (height[i-1] > height[i]) and (height[i] < height[i+1]) and (length[i] < 2*L):
            return False
        if (height[i-1] < height[i] < height[i+1]) and (length[i] < L):
            return False
        if (height[i-1] > height[i] > height[i+1]) and (length[i] < L):
            return False
        
    if (height[0] < height[1]) and (length[0] < L):
        return False
    if (height[-1] < height[-2]) and (length[-1] < L):
        return False
        
    return True

N, L = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
road = 0

# 행 체크
for i in range(N):
    if is_possible(space[i]):
        road += 1

# 열 체크
for i in range(N):
    if is_possible([row[i] for row in space]):
        road += 1

print(road)