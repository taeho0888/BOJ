for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    max_r, min_r = max(r1, r2), min(r1, r2)

    if max_r <= distance:
        if r1 + r2 > distance:
            print(2)
        elif r1 + r2 == distance:
            print(1)
        else:
            print(0)
    else: # max_r > distance
        if distance + min_r < max_r:
            print(0)
        elif distance + min_r == max_r:
            if x1 == x2 and y1 == y2:
                print(-1)
            else:
                print(1)
        else:
            print(2)
