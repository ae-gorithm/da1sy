t = int(input())

for i in range(t):
    case = list(input())    
    stack = []
    is_valid = True

    for char in case:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) == 0:
                is_valid = False
                break
            else:
                stack.pop()

    if is_valid and not stack:
        print('YES')
    else:
        print('NO')