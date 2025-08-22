import sys
from collections import deque
input=sys.stdin.readline

MAX=10**5

def bfs():
    queue=deque([subin])

    while queue:
        vertex=queue.popleft()

        if vertex==sister:
            print(distance[vertex])
            return
        
        for nx in ([vertex-1,vertex+1,2*vertex]):
            if 0<=nx<=MAX and not distance[nx]:
                distance[nx]=distance[vertex]+1
                queue.append(nx)



subin,sister=map(int,input().split())
distance=[0]*(MAX+1)


bfs()


