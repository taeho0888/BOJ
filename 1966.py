from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    count = 1
    while q:
        # 하나 빼
        doc = q.popleft()
        
        # 궁금한 문서가 빠졌을 때
        if m == 0:
            # 궁금한 문서가 제일 우선순위 높다면, 
            # 먼저 프린트된 문서 갯수 출력 후 종료
            if (len(q) == 0) or (doc >= max(q)):
                print(count)
                break
            # 더 높은 우선순위가 있다면,
            # 덱에 다시 넣고 m 초기화
            else:
                q.append(doc)
                m = len(q)-1
        # 궁금한 문서가 빠진 게 아니면, 
        # 더 높은 우선순위가 없다면 출력, count 1 증가
        elif doc >= max(q):
            m -= 1
            count += 1
        # 더 높은 우선순위가 있다면, 오른쪽에 추가
        else:
            m -= 1
            q.append(doc)
