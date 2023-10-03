# https://www.acmicpc.net/problem/2606

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(int(input())):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

infected = [False]*(N+1)
infected[1] = True
stack = [1]

while stack:
    now = stack.pop()

    for node in adj[now]:
        if not infected[node]:
            infected[node] = True
            stack.append(node)

print(sum(infected)-1)