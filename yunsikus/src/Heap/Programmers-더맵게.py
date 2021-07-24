import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    size = len(scoville)

    while True:
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            return answer
        if len(scoville) == 0:
            return -1
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + 2 * m2)
        answer += 1

    return answer
