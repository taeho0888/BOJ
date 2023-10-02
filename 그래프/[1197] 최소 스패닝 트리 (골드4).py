# https://www.acmicpc.net/problem/1197
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

V, E = map(int, input().split())

# 간선 정보 입력받기
edges = []
for _ in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

# 간선을 가중치 순으로 정렬
edges.sort()

# 각 노드에 대한 부모 테이블 초기화
parent = [i for i in range(V+1)]

# 크루스칼 알고리즘 수행
result = 0
for edge in edges:
    w, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += w

print(result)
