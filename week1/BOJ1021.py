from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, N + 1))
count = 0

for target in targets:
    idx = dq.index(target)
    
    # 왼쪽이 더 가까운 경우
    if idx <= len(dq) // 2:
        dq.rotate(-idx)  # 왼쪽으로 회전
        count += idx

    # 오른쪽이 더 가까운 경우
    else:
        dq.rotate(len(dq) - idx)  # 오른쪽으로 회전
        count += len(dq) - idx

    dq.popleft() 

print(count)