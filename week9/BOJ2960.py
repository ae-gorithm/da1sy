def remove_multiple(n, k):
    is_removed = [False] * (n + 1)
    count = 0

    for i in range(2, n + 1):
        if not is_removed[i]:
            for j in range(i, n + 1, i):
                if not is_removed[j]:
                    is_removed[j] = True
                    count += 1
                    if count == k:
                        print(j)
                        return

n, k = map(int, input().split())
remove_multiple(n, k)