# https://www.acmicpc.net/problem/
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    is_reverse = False
    is_error = False

    raw_array = input().strip()[1:-1]
    if raw_array:
        array = deque(raw_array.split(","))
    else:
        array = []

    for now in p:
        if now == "D":
            if not array:
                is_error = True
                break

            if is_reverse:
                array.pop()
            else:
                array.popleft()

        elif now == "R":
            is_reverse = not is_reverse

    if is_error:
        print('error')
    else:
        if is_reverse:
            array.reverse()
        # print(array)
        print("[" + ",".join(array) + "]")
