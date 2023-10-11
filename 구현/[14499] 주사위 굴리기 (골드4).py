# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))

direction = {
    1: [0, 1],
    2: [0, -1],
    3: [-1, 0],
    4: [1, 0]
}

dice = {
    "up": 0,
    "down": 0,
    "front": 0,
    "back": 0,
    "right": 0,
    "left": 0
}


def roll_dice(dice, dir):
    if dir == 1:
        up = dice['left']
        down = dice['right']
        front = dice['front']
        back = dice['back']
        right = dice['up']
        left = dice['down']
    elif dir == 2:
        up = dice['right']
        down = dice['left']
        front = dice['front']
        back = dice['back']
        right = dice['down']
        left = dice['up']
    elif dir == 3:
        up = dice['back']
        down = dice['front']
        front = dice['up']
        back = dice['down']
        right = dice['right']
        left = dice['left']
    else:  # dir == 4:
        up = dice['front']
        down = dice['back']
        front = dice['down']
        back = dice['up']
        right = dice['right']
        left = dice['left']

    return {
        "up": up,
        "down": down,
        "front": front,
        "back": back,
        "right": right,
        "left": left
    }


for dir in move:
    dx, dy = direction[dir]
    nx, ny = x + dx, y + dy

    if (0 > nx) or (nx >= n) or (0 > ny) or (ny >= m):
        continue

    x, y = nx, ny
    dice = roll_dice(dice, dir)

    if maps[x][y] == 0:
        maps[x][y] = dice["down"]
    else:
        dice["down"] = maps[x][y]
        maps[x][y] = 0

    print(dice["up"])
