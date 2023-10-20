# https://www.acmicpc.net/problem/10816
import sys
from bisect import bisect_left
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
card = defaultdict(int)
for num in map(int, input().split()):
    card[num] += 1
m = int(input())
input_list = list(map(int, input().split()))

for i in range(m):
    num = input_list[i]
    if num not in card:
        cur = 0
    else:
        cur = card[num]
    print(cur, end=" ")
