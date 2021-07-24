from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    final = []

    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))
        # 모든 컬럼 조합을 담는다. 컬럼이 2개면 [(0), (1), (0,1)]

    for keys in candidates:
        tmp = [tuple([rows[key] for key in keys]) for rows in relation]
        # tmp : 컬럼 index에 해당되는 컬럼값들의 모임
        if len(set(tmp)) == n_row:
        # set으로도 그 길이가 줄어들지 않는다면, 중복이 없다는듯.
            final.append(keys)
            # 중복이 없는 경우(유일성을 만족하는 경우) final에 담는다.

    answer = set(final[:])

    for i in range(len(final)-1):
    # 최소성 check를 위해, 해당 원소가 다른 원소에 포함되어있는지 확인.
        for j in range(i+1,len(final)):
            if set(final[i]) == set(final[i]) & set(final[j]):
            # 만약 포함되어 있다면 더 큰 원소를 answer에서 삭제함.
                answer.discard(final[j])

    return len(answer)
