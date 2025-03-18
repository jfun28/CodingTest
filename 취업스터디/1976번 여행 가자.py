from collections import deque
n=int(input())
m=int(input())

sightseeing=list(map(int,input().split()))

graph=[]
visited=[0]*(n)

for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(v):
    queue=deque([v])
    # 현재 위치에서 4가지 방향 위치 확인
    visited[v] = True
    while queue: 
        v=queue.popleft()
        for i in range(n):
            # 벽이 아니므로 이동 가능
            if visited[i]==0 and graph[v][i]==1:
                queue.append(i)
                visited[i]=1

        
bfs(sightseeing[0]-1)
result="YES"
for i in sightseeing:
    if visited[i-1]==0:
        result="NO"
        break

print(result)





