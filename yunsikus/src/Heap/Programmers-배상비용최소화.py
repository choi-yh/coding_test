def solution(no, works):
    works = [-1*x for x in works] 
    heapq.heapify(works)    
    while no>0:
        max_value = heapq.heappop(works)
        if max_value == 0:
            break 
        heapq.heappush(works,max_value+1)
        no -= 1
    answer = sum([x**2 for x in works])
    return answer