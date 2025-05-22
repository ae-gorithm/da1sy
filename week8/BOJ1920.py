n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))    # set -> list로 수정

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)