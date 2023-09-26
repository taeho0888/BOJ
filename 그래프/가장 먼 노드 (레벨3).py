# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
    
def solution(n, edge):
    # 그래프 생성
    adj = [[] for _ in range(n+1)]
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)

    # 최단 거리 계산
    min_distance = [0]*(n+1)
    
    visited = [False]*(n+1)
    visited[1] = True
    q = deque([(1, 0)])
    
    while q:
        now, dist = q.popleft()
        
        min_distance[now] = dist
        
        for node in adj[now]:
            if not visited[node]:
                visited[node] = True
                q.append((node, dist+1))
    
    # 정렬
    min_distance = sorted(min_distance, reverse=True)
    
    # 개수 계산
    answer = 0
    max_dist = min_distance[0]
    for d in min_distance:
        if d == max_dist:
            answer += 1

    return answer