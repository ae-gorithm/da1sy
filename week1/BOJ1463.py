# 절단기 높이가 낮을수록 잘리는 나무는 많고, 절단기 높이가 높을수록 잘리는 나무는 적음 - 이진탐색 사용하자!
# H 값을 조정해서 잘린 나무의 총합이 M 이상이 되는지

def binary_search(trees, M):
    start = 0
    end = max(trees)
    result = 0

    while start <= end:
        mid = (start + end) // 2

        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid

        if total >= M:
            result = mid  # 가능한 높이일 경우 저장
            start = mid + 1  # 더 높은 것도 가능한지 탐색
        else:
            end = mid - 1

    return result


N, M = map(int, input().split())    # 나무 개수, 필요한 나무 길이
trees = list(map(int, input().split())) # 나무 높이

print(binary_search(trees, M))