dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
table = [list(map(int,input().split())) for _ in range(N**2)]
favor = [x[1:] for x in table]
who = [x[0] for x in table]
board = [[0]*N for _ in range(N)]

s_list = {} # {4: [2, 5, 1, 7], ...}
for i in range(len(table)):
    s_list[who[i]] = favor[i]

# 1. 전체 N**2개의 사람을 차례대로 앉힌다.
for i in range(N**2):
    likes = s_list[who[i]]
    # [좋아하는 학생 개수(많), 인접 빈칸 개수(많), y, x]
    like_list = []
    for y in range(N):
        for x in range(N):
            # 2. 아직 아무도 않지 않은 칸에 대하여
            if board[y][x] == 0:
                # 3. 좋아하는 학생 개수, 인접한 빈칸의 개수, y좌표, x좌표를 기록한다.
                like_count = 0
                space_count = 0
                for k in range(4):
                    now_y = y + dy[k]
                    now_x = x + dx[k]
                    if 0<=now_y< N and 0<=now_x<N:
                        if board[now_y][now_x] in likes:
                            like_count += 1
                        elif board[now_y][now_x] == 0:
                            space_count += 1
                like_list.append([like_count, space_count, y, x])
    # 4. 1) 좋아하는 학생 개수의 내림차순, 2)인접한 빈칸의 개수의 내림차순 3) y좌표(행) 4) x좌표(열)로 정렬한다.
    like_list.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    # 5. 가장 앞에 나오는 원소의 좌표(3번째, 4번째값)에 who를 앉힌다.
    board[like_list[0][2]][like_list[0][3]] = who[i]

## 6. 점수 계산
ans = 0
for y in range(N):
    for x in range(N):
        likes = s_list[board[y][x]]
        like_count = 0
        for k in range(4):
            now_y = y + dy[k]
            now_x = x + dx[k]
            if 0<= now_y < N and 0 <= now_x < N:
                if board[now_y][now_x] in likes:
                    like_count += 1
        if like_count == 1:
            ans += 1
        elif like_count == 2:
            ans += 10
        elif like_count == 3:
            ans += 100
        elif like_count == 4:
            ans += 1000

print(ans)
