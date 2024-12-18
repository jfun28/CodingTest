# DFS와 BFS 1260
from collections import deque

n,m,v=map(int,input().split())

graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1


visited=[False]*(n+1)

def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in range(n+1):
        if visited[i]==False and graph[v][i]==1:
            dfs(i)



dfs(v)

visited2=[False]*(n+1)


def bfs(v):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque([v])
    # 현재 노드를 방문 처리
    visited2[v]=1
    while queue:
        v=queue.popleft()
        print(v, end=' ')      
        for i in range(n+1):
            if visited2[i]==False and graph[v][i]==1:
                queue.append(i)
                visited2[i]=1

print()

bfs(v)


































# graph=[[0]*(N+1) for _ in range(N+1)]

# for _ in range(M):
#     a,b= map(int,input().split())
#     graph[a][b]=graph[b][a]=1


# visited1=[0]*(N+1)
# visited2=visited1.copy()

# # dfs 함수 만들기

# def dfs(V):
#     visited1[V]=1
#     print(V,end='')
#     for i in range(1,N+1):
#         if graph[V][i]==1 and visited1[i]==0:
#             dfs(i)


# def bfs(V):
#     queue=[V]
#     visited2[V]=1 # 방문 처리
#     while queue:
#         V=queue.pop(0) # 방문 노드 제거
#         print(V,end=' ')
#         for i in range(1,N+1):
#             if (visited2[i]==0 and graph[V][i]==1):
#                 queue.append(i)
#                 visited2[i]=1


# dfs(V)
# print()
# bfs(V)