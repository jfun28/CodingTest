from collections import deque
n=int(input())

graph=list(map(int,input().split()))

print(graph)
visited=[False]*n

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        for i in range(graph[v]):
            if not visited[i]:
                queue.append(graph[i])
                visited[i]=True


    bfs(graph,0,visited)