from collections import deque

def solution(priorities, location):
    priorities = [(p,i) for i,p in enumerate(priorities)] 
    queue = deque(priorities)
    answer = 0
    while queue:
        j = queue.popleft()
        if queue and max(queue)[0] > j[0]: # 비어있는 큐에 max함수를 적용하면 error 발생
            queue.append(j)
        else:
            answer += 1
            if j[1] == location:
                break
    return answer
