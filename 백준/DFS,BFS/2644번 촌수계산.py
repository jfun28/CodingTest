num=int(input())

a,b=map(int,input().split())

n=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    x,y=map(int, input().split())
    graph[a][b]=graph[b][a]=1

visted=[False]*(n+1)

count=0
def dfs(graph,v,visited):
    global count

    visted=True
    for i in range(n+1): # a 시작해서 b를 만나면 끝난다다
        if visited[i]==False and graph[v][i]==1:
            count+=1
            dfs(graph,i, visited)
    return count

count=dfs(graph,a,visted)
print(count)