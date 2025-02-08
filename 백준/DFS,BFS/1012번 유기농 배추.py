import sys
input=sys.stdin.readline


def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    # 상하좌우 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if (0<=nx<m) or (0<=ny<n):
            if graph[ny][nx]==1:
                graph[ny][nx]=-1
                dfs(nx,ny)


t=int(input())
                
for _ in range(t):
    m,n,v=map(int,input().split())

    graph=[[0]*m for _ in range(n)]
    result=0
    for _ in range(v):
        a,b=map(int,input().split())
        graph[a][b]=graph[b][a]=1
    
    for i in range(n):
        for j in range(m):
            if graph[j][i]==1: # x축 y축 헷갈리지 말것
                dfs(i,j)
                result+=1
                
# 출력
print(result)    
