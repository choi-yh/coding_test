from collections import Counter
def solution(N, stages):
    count = Counter(stages) # 각 스테이지까지 도달한 유저의 수
    rate = {}
    delimiter = len(stages) # 각 스테이지에 도달한 유저의 수
    for stage in range(1,N+1):
        if delimiter != 0:
            rate[stage] = count[stage]/delimiter
            delimiter -= count[stage]

        # 스테이지에 도달한 유저가 없는 경우 0으로 정의
        else:
            rate[stage] = 0


    return sorted(rate, key =lambda x: rate[x], reverse=True) # value 값으로 key 값을 정렬
