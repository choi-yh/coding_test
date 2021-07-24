from collections import deque

N = int(input())
apple_n = int(input())
apple_coord = [list(map(int,input().split())) for _ in range(apple_n)]
turn_n = int(input())
turn_direction = dict()

for _ in range(turn_n): #  {8: 'D', 10: 'D', 11: 'D', 13: 'L'}
    turn, direction = input().split()
    turn_direction[int(turn)] = direction

board = [[0]*N for _ in range(N)] # 사과의 위치를 1로 채운다.
for coord_x, coord_y in apple_coord:
    board[coord_x-1][coord_y-1] = 1

turns = [x[0] for x in turn_direction.items()]  # 방향 수정이 필요한 turn을 list에 담는다.

dx = [0,-1,0,1] # right, up, left, down
dy = [1,0,-1,0]

def start():
    coord = deque()
    coord.append((0,0))
    turn = 0
    x = 0
    y = 0
    direction = 0
    while True:
        ## 방향 수정을 해야되는 경우
        if turn in turns:
            DL = turn_direction[turn]
            if DL == 'L':
                direction = (direction+1)%4
            elif DL == 'D':
                direction = (direction+3)%4

        x = x + dx[direction]
        y = y + dy[direction]

        turn += 1

        # 새로운 좌표가 board를 넘거나
        if (x >= N) or (y >= N) or (x < 0) or (y < 0):
            return

        # 지금 지나고 있는 좌표라면 stop
        if (x,y) in coord:
            return

        # 두 조건 다 해당하지 않으면, 새로운 좌표를 queue에 추가
        coord.append((x,y))

        # 사과를 먹지 않는 경우는 queue에서 제일 처음에 들어왔던 좌표를 삭제한다.
        # 사과를 먹은 경우는 아무 작업도 하지 않는다.
        if board[x][y] != 1:
            coord.popleft()

        # 사과를 먹은 경우 1을 0으로 리샛시켜준다.
        board[x][y] = 0

print(start())

