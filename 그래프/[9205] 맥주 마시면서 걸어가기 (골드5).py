# https://www.acmicpc.net/problem/9205
import sys
from collections import deque
input = sys.stdin.readline


def can_go(start, end):
    if abs(end[0] - start[0]) + abs(end[1] - start[1]) > 1000:
        return False
    return True


for _ in range(int(input())):
    answer = 'sad'
    n = int(input())
    start = tuple(map(int, input().split()))
    store = [tuple(map(int, input().split())) for __ in range(n)]
    end = tuple(map(int, input().split()))
    storend = [start] + store + [end]

    visited = [False]*len(storend)
    visited[0] = True
    q = deque([start])

    while q:
        now = q.popleft()

        if now == end:
            answer = 'happy'
            break

        for i, node in enumerate(storend):
            if not visited[i] and can_go(now, node):
                visited[i] = True
                q.append(node)

    print(answer)
