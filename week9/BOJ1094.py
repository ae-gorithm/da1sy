# 이진수로 구현하기
# x = int(input())

# count = bin(x).count('1')
# print(count)

x = int(input())

sticks = [64] 
while sum(sticks) > x:
    smallest = sticks.pop() // 2 
    sticks.append(smallest)    
    if sum(sticks) < x:
        sticks.append(smallest)  

print(len(sticks))