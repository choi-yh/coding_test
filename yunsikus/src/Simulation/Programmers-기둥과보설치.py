# 현재 상태가 가능한 구조물인지
def possible(answer):
    for build in answer:
        x = build[0]
        y = build[1]
        types = build[2]
        # 기둥
        if types == 0:
            if y == 0 or (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer:
                continue
            return False

        # 보
        else:
            if ((x,y-1,0) in answer or (x+1,y-1,0) in answer) or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            return False

    return True # 전부다 무사히 통과하면


def solution(n, build_frame):
    answer = set()
    for build in build_frame:
        x, y, types, operator = build
        # 설치
        if operator == 1:
            answer.add((x,y,types))
            if not possible(answer):
                answer.discard((x,y,types))
        # 삭제
        else:
            answer.discard((x,y,types))
            if not possible(answer):
                answer.add((x,y,types))

    list_answer = [list(x) for x in answer]

    return sorted(list_answer)
