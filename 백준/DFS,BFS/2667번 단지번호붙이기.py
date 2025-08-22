import sys
from collections import deque
input=sys.stdin.readline

def bfs(v):
    queue=deque([v])
    count = 1 
    global answer
    global visited
    while queue:
        conv=queue.popleft()
        for i in range(4):
            nx=conv[0]+dx[i]
            ny=conv[1]+dy[i]    
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if graph[nx][ny] and not visited[nx][ny] :
                count+=1
                queue.append((nx,ny))
                visited[nx][ny]=1
    answer.append(count)
    return

n=int(input())
graph=[]
visited=[[0]*n for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=[]


for _ in range(n):
    graph.append(list(map(int, input().strip())))


for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j]=1
            bfs((i,j))

answer.sort() 
print(len(answer))
for i in answer:
    print(i)