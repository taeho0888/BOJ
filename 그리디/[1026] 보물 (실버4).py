N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def calculate_S(A, B):
    result = 0
    for i in range(N):
        result += (A[i]*B[i])
    return result

sorted_A = sorted(A)
sorted_B = sorted(B, reverse=True)
print(calculate_S(sorted_A, sorted_B))