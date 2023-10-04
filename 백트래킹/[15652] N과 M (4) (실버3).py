# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())

stack = []
def dfs():
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return
    
    if stack:
        j = stack[-1]
    else:
        j = 1
    for i in range(j, N+1):
        stack.append(i)
        dfs()
        stack.pop()

dfs()