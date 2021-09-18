# https://www.acmicpc.net/problem/21943

n = int(input())
x = list(map(int, input().split()))
p, q = map(int, input().split())

def max_operation(n, x, p, q):
    x = sorted(x, reverse=True)
    nums = x[:q+1]
    
    for i in range(q+1, n):
        min_idx = nums.index(min(nums))
        nums[min_idx] += x[i]
        
    answer =1
    for num in nums:
        answer *= num
    
    return answer
    
print(max_operation(n, x, p, q))