from collections import deque
import sys

dw=[-1,1,0,0]
dh=[0,0,-1,1]

def bfs(graph,visited,start):
    queue=deque([start])
    visited[start[0]][start[1]]=0
    while queue:
        h,w=queue.popleft()
        for i in range(4):
            nh=h+dh[i]
            nw=w+dw[i]
            if nh<0 or nh>=n or nw<0 or nw>=n or visited[nh][nw]==0:
                continue
            if visited[nh][nw]==-1 and graph[nh][nw]==1:
                visited[nh][nw]=visited[h][w]+1
                queue.append((nh,nw))


input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]


for _ in range(n):
    graph.append(list(map(int,input().split())))

visited=[[-1]*m for i in range(n)]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph,visited,start)

for i in range(n):
    for j in range(m):
        print(visited[i][j],end=' ')
    print('')