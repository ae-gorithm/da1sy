def max_temp_sum(n, k, temp):
    # 처음 K일의 합을 초기값으로 설정
    current_sum = sum(temp[0:k])
    max_sum = current_sum

    # 슬라이딩 윈도우로 이동하면서 최대합 갱신
    for i in range(k, n):
        current_sum = current_sum - temp[i - k] + temp[i]
        max_sum = max(current_sum, max_sum)    
    
    return max_sum

n, k = map(int, input().split())
temp = list(map(int,input().split()))

print(max_temp_sum(n, k, temp))