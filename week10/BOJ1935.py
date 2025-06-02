n = int(input())
expression = list(input())
values = [int(input()) for _ in range(n)]

stack = []
for i in expression:
    if i.isalpha():
        stack.append(values[ord(i)-65])
    else:
        a = stack.pop()
        b = stack.pop()

        if i == '+':
            b += a
        elif i == '-':
            b -= a
        elif i == '*':
            b *= a
        elif i == '/':
            b /= a
        stack.append(b)

print('%.2f' %stack[-1])