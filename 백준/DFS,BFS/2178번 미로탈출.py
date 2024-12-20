n,m=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if graph[x][y]==1:

        global count
        count+=1
        graph[x][y]=0

        for i in range(4):
            for j in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if graph[nx][ny]==1:                
                    dfs(nx,ny)

        return True

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            






