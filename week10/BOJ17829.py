def pooling(size, x, y):
    mid = size // 2

    if size == 2:
        answer = [nums[x][y], nums[x][y+mid], nums[x+mid][y], nums[x+mid][y+mid]]
        answer.sort()
        return answer[-2]
    
    lt = pooling(mid, x, y)
    rt = pooling(mid, x+mid, y)
    lb = pooling(mid, x, y+mid)
    rb = pooling(mid, x+mid, y+mid)

    answer = [lt, rt, lb, rb]
    answer.sort()
    return answer[-2]

n = int(input())
nums = []

for i in range(n):
    temp = list(map(int, input().split()))
    nums.append(temp)

print(pooling(n, 0, 0))