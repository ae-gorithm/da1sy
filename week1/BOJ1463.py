import sys

N = int(input())

# dp[i]: 숫자 i를 1로 만드는 최소 연산 횟수
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 이전 숫자(i-1)에서 1을 빼서 만든 경우
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누어 떨어질 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어질 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
