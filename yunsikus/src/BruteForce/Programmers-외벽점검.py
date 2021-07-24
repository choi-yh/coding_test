from itertools import permutations
def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형하기
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start+length):
                if position < weak[index]:
                    # position이 해당 index의 weak부분을 점검하지 못하면
                    count += 1
                    if count > len(dist): # 더 투입이 불가능하다면
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
