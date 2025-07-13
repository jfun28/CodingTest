import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n,m=map(int,input().split())

graph=[[] for _ in range(n)]

arrive=False

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_search(start, depth, visited):
    global arrive
    visited[start]=True

    if depth==5:
        arrive=True
        return arrive

    for i in graph[start]:
        if not visited[i]:
            dfs_search(i,depth+1,visited)
    visited[start]=False # 


for i in range(n):
    visited=[False]*n
    dfs_search(i,1,visited)
    if arrive:
        break

if arrive:
    print(1)

else:
    print(0)