from collections import deque

M, N = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

queue = deque()
visited = [[False]*M for _ in range(N)]
start_point = []

for row in range(N): # 4
    for col in range(M): # 6
        if board[row][col] == 1:
            start_point.append([row, col, 0])
            visited[row][col] = True
        if board[row][col] == -1:
            visited[row][col] = True

def bfs(queue):
    count = 0
    while queue:
        x, y, value = queue.popleft()
        DELTAS = [[0,1], [0,-1], [1,0], [-1,0]]
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy
            count = value
            if (0 <= next_x < N) and (0 <= next_y < M) and not visited[next_x][next_y]:
                queue.append([next_x, next_y, count+1])
                visited[next_x][next_y] = True

    if sum(map(sum, visited)) != M*N:
        return -1
    else:
        return count


queue = deque(start_point)  
print(bfs(queue))  
