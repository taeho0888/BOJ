from collections import deque

N, K = map(int, input().split())

MAX_SIZE = 100001
visited = [False] * MAX_SIZE

def bfs():
    q = deque()
    q.append((N, 0))  # 현재 위치와 시간을 튜플로 저장

    while q:
        curr_pos, curr_time = q.popleft()

        # 동생의 위치에 도달하면 시간 반환
        if curr_pos == K:
            return curr_time

        # 걷기 및 순간이동의 경우를 고려
        for next_pos in [curr_pos-1, curr_pos+1, curr_pos*2]:
            if 0 <= next_pos < MAX_SIZE and not visited[next_pos]:
                visited[next_pos] = True
                if next_pos == curr_pos*2:  # 순간이동의 경우
                    q.appendleft((next_pos, curr_time))  # 시간이 더해지지 않으므로 앞쪽에 추가
                else:
                    q.append((next_pos, curr_time + 1))

print(bfs())