a = int(input())
board = [list(map(int,input().split())) for _ in range(a)]

# 바람의 방향에 따른 모래 비율
rate_left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
rate_down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
rate_right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
rate_up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]


## 가로 세로 2칸씩 padding을 둔다
def padding(board):
    nrow = len(board)
    board =  [[0]*nrow] + [[0]*nrow] + board + [[0]*nrow] +[[0]*nrow]
    board = [[0,0]+x+[0,0] for x in board]
    return board


def sand(x, y, board, rate):
    # board 좌표를 rate 배열과 대응할 수 있도록 좌표이동
    a,b = x-2, y-2
    temp = 0 # Y에서 빠져 나간 모래의 총 양
    for row in range(5):
        for col in range(5):
            if rate[row][col] != 0 and rate[row][col] != 'a':
                board[a+row][b+col] += board[x][y]*rate[row][col]//100
                # a의 양을 차후에 계산하기 위해 이동되는 모래의 양을 temp에 저장해둔다.
                temp += board[x][y]*rate[row][col]//100
            elif rate[row][col] == 'a':
                # a의 좌표를 기억한다.
                remain = (a+row, b+col)
    # 나머지 a 부분 처리
    board[remain[0]][remain[1]] += board[x][y] - temp
    board[x][y] = 0
    return board

board = padding(board)
turn = [x//2 for x in range(2,1000)]
breaker = False # 이중 for문 break를 위한 변수

# 시작점
x = len(board)//2
y = len(board)//2
dir = [(0,-1),(1,0),(0,1),(-1,0)] # 왼 아래 오른쪽 위
dir_ind = 0

# turn을 하는 주기가 [1,1,2,2,3,3,4,4]로 각 횟수가 끝날때마다 방향을 바꿔준다. (dir_ind에 1씩 더해준다.)
for point in turn:
    for _ in range(point):
        if x==2 and y==2: # 패딩으로 (0,0) 이 아닌 (2,2)이 종착점이 된다.
            breaker=True
            break

        dx, dy = dir[dir_ind%4][0], dir[dir_ind%4][1]
        x,y = x+dx, y+dy

        if dir_ind%4 == 0:
            board = sand(x,y,board, rate_left)
        elif dir_ind%4 == 1:
            board = sand(x,y,board, rate_down)
        elif dir_ind%4 == 2:
            board = sand(x,y, board, rate_right)
        else:
            board = sand(x,y, board, rate_up)

    if breaker:
        break

    dir_ind += 1

## 테두리 더하기
answer = 0
answer += sum([x[0] for x in board])
answer += sum([x[1] for x in board])
answer += sum([x[-1] for x in board])
answer += sum([x[-2] for x in board])
for i in [0,1,len(board)-1, len(board)-2]:
    for j in range(2,len(board)-2):
        answer += board[i][j]

print(answer)
