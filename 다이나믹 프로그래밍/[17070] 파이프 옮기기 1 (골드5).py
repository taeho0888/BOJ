house_num = int(input())
house = [list(map(int, input().split())) for _ in range(house_num)]


def search(i, j, direction):
    # 범위 밖이거나 벽인 경우
    if i >= house_num or j >= house_num or house[i][j]:
        return 0

    # 목적지 도착한 경우
    elif i == house_num-1 and j == house_num-1:
        return 1

    val1 = val2 = val3 = 0
    # 오른쪽
    if direction == 0 or direction == 1:
        if j+1 < house_num and not house[i][j+1]:
            val1 = search(i, j+1, 0)

    # 대각선
    if direction == 0 or direction == 1 or direction == 2:
        if i+1 < house_num and j+1 < house_num and not (house[i+1][j+1] or house[i][j+1] or house[i+1][j]):
            val2 = search(i+1, j+1, 1)

    # 아래
    if direction == 2 or direction == 1:
        if i+1 < house_num and not house[i+1][j]:
            val3 = search(i+1, j, 2)

    return val1 + val2 + val3


print(search(i=0, j=1, direction=0))

# Psuedo


# def 탐색():
#     if 벽 or 벗어남:
#         return 0

#     elif 도착지:
#         return 1

#     elif 오른쪽 방향:
#         if 오른쪽 가능:
#             값1 = 탐색(오른쪽)
#         elif 대각선 가능:
#             값2 = 탐색(대각선)
#         else:
#             예외처리

#     elif 대각선 방향:
#         if 오른쪽 가능:
#             탐색(오른쪽)
#         elif 대각선 가능:
#             탐색(대각선)
#         elif 아래 가능:
#             탐색(아래)
#         else:
#             예외처리

#     elif 아래 방향:
#         if 대각선 가능:
#             탐색(대각선)
#         elif 아래 가능:
#             탐색(아래)
