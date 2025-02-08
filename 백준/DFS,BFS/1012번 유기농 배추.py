import sys
input=sys.stdin.readline

t=int(input())

def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    # 상하좌우 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if (0<=nx<n) or (0<=ny<m):
            if graph[nx][ny]==1:
                graph[nx][ny]=-1
                dfs(nx,ny)
                
for _ in range(t):
    n,m,v=map(int,input().split())

    graph=[[0]*m for _ in range(n)]

    for _ in range(v):
        a,b=map(int,input().split())
        graph[a][b]=graph[b][a]=1
        
    visited=[[False]*m for _ in range(n)]
123