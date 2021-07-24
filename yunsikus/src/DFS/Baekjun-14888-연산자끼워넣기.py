mport sys

def dfs(val, index, plus, minus, mul, div):
    global n, maxv, minv
    if index == n:
        minv = min(val, minv)
        maxv = max(val, maxv)
        return

    if plus:
        dfs(val+input_list[index], index+1, plus-1, minus, mul, div)
    if minus:
        dfs(val-input_list[index], index+1, plus, minus-1, mul, div)
    if mul:
        dfs(val*input_list[index], index+1, plus, minus, mul-1, div)
    if div:
        dfs(int(val /input_list[index]), index+1, plus, minus, mul, div-1)

if __name__ == "__main__":
    minv = sys.maxsize
    maxv = -sys.maxsize-1
    n = int(input()) # 2
    input_list = list(map(int ,input().split())) # [5, 6]
    a, b, c, d = map(int, input().split()) # 0, 0, 1, 0
    dfs(input_list[0], 1, a, b, c, d)
    print(maxv) # 30
    print(minv) # 30
