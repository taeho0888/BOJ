N = int(input())
line = sorted(list(map(int, input().split())))

wait_time = [0]*N
for i in range(N):
    for j in range(i, N):
        wait_time[j] += line[i]

print(sum(wait_time))
