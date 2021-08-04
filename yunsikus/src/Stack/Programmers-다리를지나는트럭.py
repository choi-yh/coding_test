from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0]*(bridge_length)) # list의 pop(0)는 O(n) 반면, deque 자료구조의 leftpop()은 O(1) 이다. 
    time = 0
    sum_bridge = 0 # sum(bridge) 대신 계산 과정에서 bridge를 매번 계산하여 넘긴다. 

    while bridge:
        time += 1
        sum_bridge -= bridge[0]
        bridge.popleft()
        if truck_weights:
            sum_bridge += truck_weights[0]
            if sum_bridge <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
                sum_bridge -= truck_weights[0]

    return time