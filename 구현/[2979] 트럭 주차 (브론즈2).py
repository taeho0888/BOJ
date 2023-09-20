# https://www.acmicpc.net/problem/2979

A, B, C = map(int, input().split())
time = [0]*101

for _ in range(3):
    a, b = map(int, input().split())
    for i in range(a, b):
        time[i] += 1

answer = 0
for t in time:
    if t == 0:
        continue
    elif t == 1:
        answer += A
    elif t == 2:
        answer += B*2
    else:
        answer += C*3

print(answer)