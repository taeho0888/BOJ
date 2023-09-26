# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations, permutations
input = sys.stdin.readline

def team_stat(team):
    sum_stat = 0
    for pmt in permutations(team, 2):
        sum_stat += stat[pmt[0]-1][pmt[1]-1]
    return sum_stat

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
for team1 in combinations([i for i in range(1, N+1)], int(N/2)):
    team2 = tuple(i for i in range(1, N+1) if i not in team1)
    dif = abs(team_stat(team1) - team_stat(team2))
    answer = min(answer, dif)

print(answer)