# dfs
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
count = 1

def dfs(graph, r, visited, order):
    global count
    visited[r] = True         
    order[r] = count             
    count += 1                   

    # 인접 노드를 방문하지 않았다면 계속 탐색
    for i in graph[r]:           
        if not visited[i]:       
            dfs(graph, i, visited, order) 

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
order = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()
 
dfs(graph, r, visited, order)

for i in range(1, n + 1):
    print(order[i])