import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    queue=deque([subin])
    while queue:
        x=queue.popleft()
        if x==sister:
            print(dist[x])
            break

        for nx in (x-1,x+1,2*x):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx]=dist[x]+1
                queue.append(nx)
                

MAX=10**5

subin, sister=map(int,input().split())

dist=[0]*(MAX+1)


bfs()

