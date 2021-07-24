N, M, x, y, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dir_arr = list(map(int,input().split()))

dx = [0, 0, -1, 1] # 동, 서, 북, 남
dy = [1, -1, 0, 0]

def check(x, y, dir): # 바깥으로 나가는 경우를 제외하기 위해
    new_x = x+dx[dir-1]
    new_y = y+dy[dir-1]
    if (0 <= new_x < N) and (0 <= new_y < M):
        return True

def move(direction, board, dice, x, y):
    if direction == 3: # up
        dice[0], dice[5] = dice[5], dice[0] # 주사위의 첫번째 원소와 여섯번째 원소를 바꾼다
        dice[2], dice[5] = dice[5], dice[2] # 세번쨰와 여섯번째 원소를 바꾼다
        dice[4], dice[5] = dice[5], dice[4] # 다섯번째와 여섯번째 원소를 바꾼다
        x -= 1
        if board[x][y] == 0:
            board[x][y] = dice[2]
        else:
            dice[2] = board[x][y]
            board[x][y] = 0
        return board, dice, x, y

    if direction == 4: # down
        dice[0], dice[2] = dice[2], dice[0]
        dice[2], dice[4] = dice[4], dice[2]
        dice[4], dice[5] = dice[5], dice[4]
        x += 1
        if board[x][y] == 0:
            board[x][y] = dice[2]
        else:
            dice[2] = board[x][y]
            board[x][y] = 0
        return board, dice, x, y

    if direction == 2: # left
        dice[1], dice[5] = dice[5], dice[1]
        dice[2], dice[5] = dice[5], dice[2]
        dice[3], dice[5] = dice[5], dice[3]
        y -= 1
        if board[x][y] == 0:
            board[x][y] = dice[2]
        else:
            dice[2] = board[x][y]
            board[x][y] = 0
        return board, dice, x, y

    if direction == 1: # right
        dice[1], dice[2] = dice[2], dice[1]
        dice[2], dice[3] = dice[3], dice[2]
        dice[3], dice[5] = dice[5], dice[3]
        y += 1
        if board[x][y] == 0:
            board[x][y] = dice[2]
        else:
            dice[2] = board[x][y]
            board[x][y] = 0
        return board, dice, x, y

dice = [0,0,0,0,0,0]
for dir in dir_arr:
    if check(x, y, dir): # 바깥으로 나가지 않는 경우
        board, dice, x, y = move(dir, board, dice, x, y)
        print(dice[5])
