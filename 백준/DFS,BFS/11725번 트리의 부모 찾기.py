import sys

from collections import deque
input=sys.stdin.readline

n=int(input())

vertices=[[0] for _ in range(n+1)]
parent=[0]*(n+1)

for _ in range(1,n):
    a,b=map(int,input().split())
    vertices[a].append(b)
    vertices[b].append(a)

parent[1]=0

q=deque()
q.append(1)

while q:
    current=q.popleft()
    for ver in vertices[current]:
        if parent[ver]==0:
            parent[ver]=current
            q.append(ver)

for i in parent[2:]:
    print(i)
