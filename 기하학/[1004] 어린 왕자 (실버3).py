import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    for i in range(int(input())):
        cx, cy, r = map(int, input().split())
        d1 = (((cx-x1)**2 + (cy-y1)**2)**0.5) <= r
        d2 = (((cx-x2)**2 + (cy-y2)**2)**0.5) <= r
        if (d1 and not d2) or (not d1 and d2):
            count += 1

    print(count)

    