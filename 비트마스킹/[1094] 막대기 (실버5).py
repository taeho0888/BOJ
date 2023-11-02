# https://www.acmicpc.net/problem/1094

x = int(input())
answer = 0
for i in bin(x):
    if i == "1":
        answer += 1
print(answer)
