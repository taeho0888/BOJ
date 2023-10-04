# https://www.acmicpc.net/problem/15649
from itertools import permutations

N, M = map(int, input().split())

for pmt in permutations([i for i in range(1, N+1)], M):
    print(*pmt)