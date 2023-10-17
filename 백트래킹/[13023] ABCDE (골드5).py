# https://www.acmicpc.net/problem/13023
def dfs():
    global flag

    if len(stack) == 5:
        flag = True
        return

    for next in adj[stack[-1]]:
        if next not in stack:
            stack.append(next)
            dfs()
            stack.pop()


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

flag = False
stack = []
for i in range(n):
    if flag:
        break
    stack.append(i)
    dfs()
    stack.pop()

if flag:
    print(1)
else:
    print(0)
