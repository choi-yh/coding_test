def is_possible(lamps, road_length, light):
    # case 1
    if lamps[0] - light > 0:
        return False
    # case 2
    if lamps[-1] + light < road_length:
        return False

    # case 3
    for i in range(len(lamps)-1):
        if lamps[i] + light*2 < lamps[i+1]:
            return False
    return True

# 하한선 템플릿
def solution(lamps, road_length):
    lower = 0
    upper = road_length
    lamps.sort()
    print(lamps)
    while lower <= upper:
        mid = (lower + upper) // 2
        print(mid)
        if is_possible(lamps, road_length, mid):
            upper = mid - 1
        else:
            lower = mid + 1
    return upper + 1
