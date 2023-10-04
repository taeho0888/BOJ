N = int(input())
answer = 0
def possible(queen, x, y):
    for qx, qy in queen:
        if qx == x:
            return False
        if qy == y:
            return False
        if qx - qy == x - y:
            return False
        if qx + qy == x + y:
            return False
    
    return True

def dfs(queen, i):
    global answer

    if i == N:
        answer += 1
        return
    
    for j in range(N):
        if possible(queen, i, j):
            queen.append((i, j))
            dfs(queen, i+1)
            queen.pop()

dfs([], 0)
print(answer)
