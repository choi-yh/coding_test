from collections import deque

def solution(progresses, speeds):
    answer = []
    complete = [-1*((p-100)//s) for p,s in zip(progresses, speeds)]
    queue = deque(complete)
    while queue:
        val = queue.popleft()
        n = 1
        while queue and val >= queue[0]:
            n += 1
            queue.popleft()
        answer.append(n)
    return answer
