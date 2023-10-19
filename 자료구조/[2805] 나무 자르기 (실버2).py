# https://www.acmicpc.net/problem/2805
n, m = map(int, input().split())
tree = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 0, max(tree)
answer = 0

while start <= end:
    mid = (start + end) // 2  # 절단기의 높이 설정

    # 잘린 나무의 총 길이 계산
    total = sum([t - mid for t in tree if t > mid])

    # 잘린 나무의 길이가 필요한 길이보다 작은 경우
    if total < m:
        end = mid - 1
    # 잘린 나무의 길이가 필요한 길이보다 크거나 같은 경우
    else:
        answer = mid  # 가능한 절단기 높이 저장
        start = mid + 1

print(answer)
