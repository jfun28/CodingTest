from collections import deque

n,m=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=0

def bfs(x,y):
    queue=deque()
   
    queue.append((x,y))
    # 현재 위치에서 4가지 방향 위치 확인
    while queue: 
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 위치 벗어나면 안되므로 조건 추가
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            # 벽이 아니므로 이동 가능
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
    
            





