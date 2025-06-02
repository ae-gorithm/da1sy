# 브루트포스 - O(N²) 시간 초과 / 10,000 × 10,000 = 1억 번 연산이 발생
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# count = 0

# for i in range(n):
#     sum = 0

#     for j in range(i, n):
#         sum += a[j]
#         if sum == m:
#             count += 1
#         elif sum > m:
#             break

# print(count)

# 투 포인터 - O(N)
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0
start, end = 0, 0
current_sum = 0

while(True):
    if current_sum >= m:
        current_sum -= a[start]
        start += 1
    
    elif end == n:
        break

    else:
        current_sum += a[end]
        end += 1

    if current_sum == m:
        count += 1
    
print(count)
