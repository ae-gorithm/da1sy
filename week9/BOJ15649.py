def backtrack(n, m, visited, sequence):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            backtrack(n, m, visited, sequence)
            sequence.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n + 1)
backtrack(n, m, visited, [])