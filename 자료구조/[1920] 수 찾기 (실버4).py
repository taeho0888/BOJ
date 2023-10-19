# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

n = int(input())
num_set = set(map(int, input().split()))
m = int(input())
for num in list(map(int, input().split())):
    if num in num_set:
        print(1)
    else:
        print(0)
