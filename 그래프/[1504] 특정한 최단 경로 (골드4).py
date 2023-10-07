# https://www.acmicpc.net/problem/1504
import heapq

N, E = map(int, input().split())
graph = {i: {} for i in range(N+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w
v1, v2 = map(int, input().split())


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if cur_dist > distances[cur_node]:
            continue

        for adj, weight in graph[cur_node].items():
            dist = weight + cur_dist
            if distances[adj] > dist:
                distances[adj] = dist
                heapq.heappush(queue, [dist, adj])

    return distances


dist_from_1_to = dijkstra(graph, 1)
dist_from_v1_to = dijkstra(graph, v1)
dist_from_v2_to = dijkstra(graph, v2)

way1 = dist_from_1_to[v1] + dist_from_v1_to[v2] + dist_from_v2_to[N]
way2 = dist_from_1_to[v2] + dist_from_v2_to[v1] + dist_from_v1_to[N]
answer = min(way1, way2)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
