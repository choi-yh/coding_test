def solution(numbers, target):
    answer = 0
    def dfs(n, value):
        nonlocal answer
        if n == len(numbers):
            if value == target:
                answer += 1
            return
        dfs(n+1, value+numbers[n])
        dfs(n+1, value-numbers[n])
    dfs(0,0)
    return answer