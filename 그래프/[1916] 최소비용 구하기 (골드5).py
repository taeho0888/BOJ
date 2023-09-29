# https://www.acmicpc.net/problem/1916
import heapq

N = int(input())
M = int(input())
graph = {i: {} for i in range(1, N+1)}
for _ in range(M):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w
A, B = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {i: float('inf') for i in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if distances[cur_node] < cur_dist:
            continue

        for adj, weight in graph[cur_node].items():
            dist = cur_dist + weight
            if distances[adj] > dist:
                distances[adj] = dist
                heapq.heappush(queue, [dist, adj])
    
    return distances[end]


print(dijkstra(graph, A, B))