# 백트래킹
import sys

def backtrack(index, sour, bitter, count):
    global min_diff

    if index == n:
        if count > 0:
            min_diff = min(min_diff, abs(sour - bitter))
        return
    
    # 선택했을 때
    backtrack(index + 1, sour * ingredient[index][0], bitter + ingredient[index][1], count + 1)
    # 선택하지 않았을 때
    backtrack(index + 1, sour, bitter, count)

n = int(input())
ingredient = [list(map(int, input().split())) for _ in range(n)]

min_diff = sys.maxsize
backtrack(0,1,0,0)

print(min_diff)

