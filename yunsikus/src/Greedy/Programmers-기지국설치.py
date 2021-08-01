import math

def solution(n, stations, w):
    covered = 0
    width = 2 * w + 1
    answer = 0
    for station in stations:
        lower = station - w
        upper = station + w
        if covered <= lower: # 커버하지 못한 부분이 남아있으면
            answer += math.ceil((lower - 1 - covered) / width)
        covered = upper
    if covered <= n: # 커버하지 못한 부분이 남아있으면
        answer += math.ceil((n - covered) / width)


    return answer