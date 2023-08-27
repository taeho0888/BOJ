# 내 풀이

A = int(input())
B = int(input())

print(A*(B % 10))
print(int(A*(B % 100-B % 10)*0.1))
print(int(A*(B-B % 100)*0.01))
print(A*B)
