from collections import deque
N, K = map(int, input().split())
MAX_LEN = 100_001
visited = [False]*MAX_LEN
q = deque([(N, 0)])

while q:
    n, count = q.popleft()
    if n == K:
        print(count)
        exit()

    if n+1 < MAX_LEN and not visited[n+1]:
        visited[n+1] = True
        q.append((n+1, count+1))
    if n-1 >= 0 and not visited[n-1]:
        visited[n-1] = True
        q.append((n-1, count+1))
    if n*2 < MAX_LEN and not visited[n*2]:
        visited[n*2] = True
        q.append((n*2, count+1))
