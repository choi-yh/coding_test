
from collections import deque
def solution(maps):
    DELTAS = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque()
    height = len(maps) # 행
    width = len(maps[0]) # 열
    visited = [[-1]*width for _ in range(height)]
    queue.append((0,0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in DELTAS:
            nx = x + dx
            ny = y + dy
            nv = visited[x][y] + 1
            if (0 <= nx < height) and (0 <= ny < width): # 게임 맵을 벗어난 경우
                if maps[nx][ny] > 0 and visited[nx][ny] == -1: # bloack되거나 이미 방문한 경우에는
                    queue.append([nx, ny])
                    visited[nx][ny] = nv

    return visited[height-1][width-1]