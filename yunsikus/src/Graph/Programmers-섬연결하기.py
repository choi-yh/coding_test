def solution(n,costs):
    def find(u): ## u 정점의 루트 노드 탐색
        if u != p[u]: ## u가 루트 노드가 아니면
            p[u] = find(p[u]) # 3 -> 2, 2 -> 1 일 경우 3 -> 1 로 경로 압축
        return p[u] ## u가 루트 노트이면 u 반환

    def union(u, v):
        root1 = find(u) # B'
        root2 = find(v)  # A'
        p[root2] = root1 # A'의 부모느드를 B'로 변경
        
    costs.sort(key = lambda x: x[2])
    p = [0] # 상호배타적 집합
    tree_edges = 0 # 간선 개수
    mst_cost = 0  # 가중치 합

    for i in range(1, n+1):
        p.append(i)
        
    while True:
        if tree_edges == n-1:
            break
        u, v, wt= costs.pop(0)
        if find(u) != find(v): # 두 노드의 루트 노드가 다르다면 두 노드가 포함되어 있는 집합을 하나로 결합
            union(u,v)
            mst_cost += wt
            tree_edges += 1
    return mst_cost