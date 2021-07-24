def solution(places):
    answer = []
    def check(matrix, x, y, turn):
        nonlocal flag
        if  matrix[x][y] == 'P' and turn != 0:
            flag = False
            return

        if turn == 2:
            return 
        
        matrix[x][y] = 'X'
        
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >=0 and nx<5 and ny >= 0 and ny <5:
                if matrix[nx][ny] != 'X':
                    check(matrix, nx, ny, turn+1)

    for place in places:
        flag = True
        my_mat = [list(x) for x in place]
        p_cord = []
        for i in range(5):
            for j in range(5):
                if my_mat[i][j] == 'P':
                    p_cord.append([i,j])

        for cord in p_cord:
            check(my_mat, cord[0], cord[1], 0)

        if not flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer