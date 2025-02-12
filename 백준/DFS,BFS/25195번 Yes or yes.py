import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[0]*(m+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

visited=[False]*(n+1)
fan_num=int(input())
fan_list=[0]*(n+1)

fan=list(map(int,input().split()))
for i in fan:
    fan_list[i]=1


def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if visited[i]==False and graph[v][i]==1:
            if fan_list[i]==1:
                count+=1
            dfs(i)
    return count
count=dfs(1)

print("Yes" if not count == 0 else "yes")

