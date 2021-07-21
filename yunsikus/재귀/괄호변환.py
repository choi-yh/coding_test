from collections import deque

def check(p):  # 올바른 괄호 문자열인지 확인하는 함수
    count = 0
    for bracket in p:
        if bracket == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return True


def solution(p):
    stack = deque(list(p))
    # 과정 1
    if not p:
        return ''

    # 만약 p가 이미 "올바른 괄호 문자열"이면 return
    if check(p):
        return ''.join(p)

    # 과정 2 - u,v 분리
    count = 0
    u = []
    for _ in range(len(p)):
        a = stack.popleft()
        if a == "(":
            count += 1
        else:
            count -= 1
        u.append(a)
        if count == 0:
            break

    u = ''.join(u)  
    v = ''.join(stack)

    # 과정 3
    if check(u):
        return u + solution(v)

    # 과정 4
    else:
        # 과정 4-1, 4-2, 4-3
        answer = "(" + solution(v) + ")"
        # 과정 4-4
        u = u[1:-1]
        for bracket in u:
            answer += ''.join(['(' if x==')' else ')' for x in bracket])

        return answer 