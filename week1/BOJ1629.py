import sys

def modPow(A, B, C):
    if B == 0:
        return 1
    if B == 1:
        return A % C

    half = modPow(A, B // 2, C)
    result = (half * half) % C

    if B % 2 == 1:
        result = (result * A) % C

    return result

A, B, C = map(int, sys.stdin.readline().split())
print(modPow(A, B, C))
