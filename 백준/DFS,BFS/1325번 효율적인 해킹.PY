from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

count=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
  


for i in range(n+1):
    q=deque()
    q.append(i)

    visited = [False] * (n + 1) 
    visited[i] = True

    while q:
        current=q.popleft()
        count[i]+=1
        for v in graph[current]:
            if not visited[v]:
                visited[v]=True
                q.append(v)

max_value=max(count)
max_indices=[i for i,v in enumerate(count) if v==max_value]

print(*max_indices) 

