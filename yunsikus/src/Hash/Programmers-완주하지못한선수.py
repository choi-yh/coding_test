# 방법 1 (Counter 사용)
from collections import Counter

def solution(participant, completion):
    player = Counter(participant) - Counter(completion)

    return list(player.keys())[0]


# 방법 2 (sort 사용)
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, comp in zip(participant, completion):
        if part != comp:
            return part

    return participant[-1]