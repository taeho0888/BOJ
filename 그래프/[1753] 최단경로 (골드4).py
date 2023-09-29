import heapq

V, E = map(int, input().split())
K = int(input())
graph = {i: {} for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
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

    return distances

distances = dijkstra(graph, K)
for key, val in distances.items():
    if val == float('inf'):
        print("INF")
    else:
        print(val)