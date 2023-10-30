# https://www.acmicpc.net/problem/2108
from collections import Counter

# 입력받기
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 산술평균 계산
mean = round(sum(numbers) / N)

# 중앙값 계산
sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

# 최빈값 계산
counter = Counter(sorted_numbers)
modes = counter.most_common()
if len(modes) > 1 and modes[0][1] == modes[1][1]:  # 최빈값이 여러 개 있는 경우
    mode = modes[1][0]
else:
    mode = modes[0][0]

# 범위 계산
range_value = max(numbers) - min(numbers)

# 결과 출력
print(mean)
print(median)
print(mode)
print(range_value)
