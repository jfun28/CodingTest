import sys

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[]*n for i in range(n)]

arrive = False

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs_search(start,depth):
    global arrive
    visited[start]=True
    if depth==5:
        arrive=True
        return arrive
    
    for i in graph[start]:
        if visited[i]==False:
            dfs_search(i,depth+1)
    visited[start]=False

    return


for i in range(n):
    visited=[False]*n
    visited[i]=True
    dfs_search(i,1)
    if arrive:
        break


if arrive:
    print(1)
else:
    print(0) 

