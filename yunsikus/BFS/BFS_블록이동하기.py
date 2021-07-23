from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        if board[pos1_x + dx[i]][pos1_y + dy[i]] == 0 and board[pos2_x + dx[i]][pos2_y + dy[i]] == 0:
            next_pos.append({(pos1_x+dx[i], pos1_y+dy[i]),(pos2_x+dx[i], pos2_y+dy[i])})

    # 가로로 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위, 아래를 확인해야함
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x+i, pos2_y)})

    if pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽, 오른쪽을 확인해야함
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x, pos2_y+i)})

    return next_pos

def solution(board):
    # 맵의 외곽에 1로 벽을 생성한다.
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # bfs 수행
    queue = deque()
    visited = []
    start_point = {(1,1),(1,2)} # 패딩으로 인해 start point도 변한다.
    queue.append((start_point,0)) # 큐에 삽입
    visited.append(start_point) # 방문 처리

    while queue:
        pos, count = queue.popleft()
        # n,n에 위치했다면 최단 거리이므로 return
        if (n,n) in pos:
            return count
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                queue.append((next_pos, count+1))
                visited.append(next_pos)
