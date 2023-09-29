# https://www.acmicpc.net/problem/1238
import heapq

N, M, X = map(int, input().split())
graph = {i: {} for i in range(1, N+1)}
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] = w

def min_dist(start, end):
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if distances[cur_node] < cur_dist:
            continue
        
        for adj, weight in graph[cur_node].items():
            dist = cur_dist + weight
            if dist < distances[adj]:
                distances[adj] = dist
                heapq.heappush(queue, [dist, adj])

    return distances[end]


answer = -1
for i in range(1, N+1):
    answer = max(answer, min_dist(i, X) + min_dist(X, i))

print(answer)