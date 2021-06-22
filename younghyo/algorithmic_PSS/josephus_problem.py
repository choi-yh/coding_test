# https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())

array = [i for i in range(1, n+1)]
result = []

while len(array) != 0:
    if len(array) >= k:
        result.append(str(array[k-1]))
        array = array[k:] + array[:k-1]
    elif len(array) == 1:
        result.append(str(array.pop()))
    else: # 남은 병사 수가 k보다 작은 경우
        remove_index = k % len(array) - 1
        result.append(str(array[remove_index]))
        array = array[remove_index+1:] + array[:remove_index]
    
josephus = '<' + ', '.join(result) + '>'
print(josephus)
