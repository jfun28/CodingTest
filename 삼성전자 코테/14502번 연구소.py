# bfs 
# 어떻게 3개를 정할 것인가?-> 랜덤하게 3개를 배치하는 것인가
from collections import deque
from itertools import combinations

height,width=map(int,input().split())
graph=[]
empty=[]
vrs=deque()

for h in range(height):
    arr = list(map(int, input().split()))
    for w in range(width):
        if arr[w]==2:
            vrs.append((h,w))

        if arr[w]==0:
            empty.append((h,w))

    graph.append(arr)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(vgraph,vrs):
    queue=deque(vrs)
    visited=[[0]*width for i in range(height)]
    for h,w in queue:
        visited[h][w] = 1


    while queue:
        h,w=queue.popleft()
        for i in range(4):
            nx=w+dx[i]
            ny=h+dy[i]
            if 0<=nx<width and 0<=ny<height:
                if visited[ny][nx]==0 and vgraph[ny][nx]==0: # 빈공간속 바이러스 전파
                    vgraph[ny][nx]=2
                    visited[ny][nx]=1
                    queue.append((ny,nx))

    return vgraph

safe=0

for a,b,c in combinations(empty, 3):
    #graph를 vgraph에 복사
    vgraph = [row[:] for row in graph]  # Correct deep copy
    
    for h,w in [a,b,c]: #벽 3개 치기
        vgraph[h][w] = 1

    vgraph = bfs(vgraph,vrs)
    zero = 0
    for i in vgraph:
        for j in i:
            if j==0:
                zero += 1
    safe = max(safe, zero)

print(safe)