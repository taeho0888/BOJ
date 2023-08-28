n, m, v = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(n,m,v)
print(edges)

def dfs(v, visited):
    if not visited[v]:
        visited[v] = True
        for edge in edges:
            if edge[0] == v:
                print(edge[1])
                dfs(edge[1], visited)

def bfs(v, visited):
    pass

print(dfs(v, [False]*n))
print(bfs(v, [False]*n))