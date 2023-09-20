def rotate_gear(gear, direction):
    if direction == 1:
        return gear[-1] + gear[:-1]
    elif direction == -1:
        return gear[1:] + gear[0]
    else:
        return gear


gear1 = input().strip()
gear2 = input().strip()
gear3 = input().strip()
gear4 = input().strip()

K = int(input())
for _ in range(K):
    gear, direction = map(int, input().split())
    is_one_equal_two = (gear1[2] == gear2[6])
    is_two_equal_three = (gear2[2] == gear3[6])
    is_three_equal_four = (gear3[2] == gear4[6])
    is_one_rotate = 0
    is_two_rotate = 0
    is_three_rotate = 0
    is_four_rotate = 0

    if gear == 1:
        is_one_rotate = direction
        if not is_one_equal_two:
            is_two_rotate = -1*direction
            if not is_two_equal_three:
                is_three_rotate = direction
                if not is_three_equal_four:
                    is_four_rotate = -1*direction
    elif gear == 2:
        is_two_rotate = direction
        if not is_one_equal_two:
            is_one_rotate = -1*direction
        if not is_two_equal_three:
            is_three_rotate = -1*direction
            if not is_three_equal_four:
                is_four_rotate = direction
    elif gear == 3:
        is_three_rotate = direction
        if not is_three_equal_four:
            is_four_rotate = -1*direction
        if not is_two_equal_three:
            is_two_rotate = -1*direction
            if not is_one_equal_two:
                is_one_rotate = direction
    else: # gear == 4
        is_four_rotate = direction
        if not is_three_equal_four:
            is_three_rotate = -1*direction
            if not is_two_equal_three:
                is_two_rotate = direction
                if not is_one_equal_two:
                    is_one_rotate = -1*direction

    gear1 = rotate_gear(gear1, is_one_rotate)
    gear2 = rotate_gear(gear2, is_two_rotate)
    gear3 = rotate_gear(gear3, is_three_rotate)
    gear4 = rotate_gear(gear4, is_four_rotate)

# 점수 구하기
print(int(gear1[0]) + int(gear2[0])*2 + int(gear3[0])*4 + int(gear4[0])*8)