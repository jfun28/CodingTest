import sys
sys.setrecursionlimit(10**6) # 이게 중요하다 
input = sys.stdin.readline


def dfs(x,y):
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]
    
    # 상하좌우 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:

            graph[ny][nx]=-1
            dfs(nx,ny)


t=int(input())
                
for _ in range(t):
    m,n,v=map(int,input().split())

    graph=[[0]*m for _ in range(n)]
    result=0
    for _ in range(v):
        a,b=map(int,input().split())
        graph[b][a]=1
    
    for i in range(m): # x축(열) 
        for j in range(n): # x축(행)
            if graph[j][i]==1: # 이차원 배열에서는 [행][열]
                dfs(i,j)
                result+=1
    # 출력
    print(result)  
     


