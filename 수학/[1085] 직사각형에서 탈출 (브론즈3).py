w, h, x, y = map(int, input().split())
print(min(x-w, w, y-h, h))