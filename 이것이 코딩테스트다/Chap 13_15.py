# 특정 거리의 도시 찾기
from collections import deque
import sys

N, M, K, X=map(int,input().split())

graph = [[] for _ in range(N+1)]
for num in range(M):
    v, t=map(int,sys.stdin.readline().split())
    graph[v].append(t)  

distance = [[] for _ in range(N+1)]
visited=[False]*(N+1)


def bfs(start):
    answer=[]
    q=deque([start]) # deque 선언할 때는 원래 리스트 형태로 선언해줘야한다. 
    visited[start]=True
    distance[start]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                distance[i]=distance[now]+1
                if distance[i]==K:
                    answer.append(i)
    if len(answer)==0:
        print(-1)
    else: 
        answer.sort()
        for i in answer:
            print(i,end='\n')


bfs(X)    














# # 특정 거리의 도시 찾기
# from  collections import deque

# def bfs(start_node, graph):
#     queue=deque([start_node])
#     visited=set([start_node])

#     while queue:
#         curr_node=queue.popleft()
#         print(curr_node," ")
#         for next_node in graph[curr_node]:
#             if next_node not in visited:
#                 visited.add(next_node)
#                 queue.append(next_node)

#     return -1


# N, M, K, X=map(int,input().split())

# graph = [[] for _ in range(N+1)]
# for num in range(M):
#     v, t=map(int,input().split())
#     graph[v].append(t)   

# print(graph)

# print("방문순서")
# bfs(1,graph)
