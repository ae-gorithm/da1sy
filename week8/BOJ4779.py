def cantor(n):
    if n == 0:
        return '-'
    prev = cantor(n - 1)
    return prev + ' ' * len(prev) + prev

while True:
    try:
        n = int(input())
        print(cantor(n))
    except:
        break