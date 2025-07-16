import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

tree=[[] for _ in range(n+1)]
parent=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

parent[1]=0
q=deque()
q.append(1)

while q:
    current=q.popleft()
    for i in tree[current]:
        if parent[i]==0:
            parent[i]=current
            q.append(i)


for i in parent[2:]:
    print(i)
