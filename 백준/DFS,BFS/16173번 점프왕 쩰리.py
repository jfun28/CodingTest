n=int(input())


def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n or visited[y][x]==1:
        return
    
    if graph[y][x]==-1:
        visited[y][x]=1
        return
        
    visited[y][x]=1

    dfs(x,y+graph[y][x])
    dfs(x+graph[y][x],y)


graph=[]


for _ in range(n):
    graph.append(list(map(int,input().split())))


visited=[[0]*n for i in range(n)]

dfs(0,0)
                        
if visited[n-1][n-1]==1:
    print("HaruHaru")
else:
    print("Hing")