# input 정보 받기
N = int(input())
M = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

travel_list = list(map(int, input().split()))

# 각 경로의 parent 노드
p = [0]
for i in range(1, N+1):
    p.append(i)

# union-find 함수 정의
def find(u): ## u 정점의 루트 노드 탐색
    if u != p[u]: ## u가 루트 노드가 아니면
        p[u] = find(p[u]) # 3 -> 2, 2 -> 1 일 경우 3 -> 1 로 경로 압축
    return p[u] ## u가 루트 노트이면 u 반환

def union(u, v):
    root1 = find(u) # B'
    root2 = find(v)  # A'
    p[root2] = root1 # A'의 부모느드를 B'로 변경

# 인덱스 번호가 작은 정점을 인덱스 번호가 큰 정점의 부모로 Union
for i in range(0, N):
    for j in range(1+i, N): #곂치는 부분은 반복 안하기 위해 j 설정
        if matrix[i][j] == 1:
            union(i+1, j+1)

# 최상위 정점이 모두 같으면 YES, 하나라도 다르면 NO
answer = set([find(x) for x in travel_list])
if len(answer) == 1:
    print('YES')
else:
    print('NO')
