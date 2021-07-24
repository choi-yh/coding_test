def dfs(x, y, d):
    global answer
    if not matrix[x][y]:
        answer += 1
        matrix[x][y] = 2

    for _ in range(4):
        d = (d+3)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if not matrix[nx][ny]: # 하나라도 0이 발견되면 다시 그 좌표에서 dfs 시작
            dfs(nx, ny, d)
            return
    nd = (d+2)%4 # 4방향에서 모두 0이 발견 안되면 뒤쪽 좌표 확인
    nx = x + dx[nd]
    ny = y + dy[nd]
    if matrix[nx][ny] == 1: # 만약 뒤쪽이 벽이면 return
        return
    dfs(nx, ny, d) # 뒤쪽이 벽이 아니면 그 방향으로 이당하여 dfs시작

if __name__ == "__main__":   
    m, n = map(int,input().split())
    r, c, d = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(m)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = 0
    dfs(r, c, d)
    print(answer)
