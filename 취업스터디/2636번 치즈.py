from collections import deque
import sys
input=sys.stdin.readline

rows, widths=map(int,input().split())

graph=[]
for _ in range(rows):
    graph.append(list(map(int,input().split())))

melt_history=[]
time=0

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append((0,0))
    visited[0][0]=True
    cnt=0

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<widths and 0<=ny<rows and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    q.append((ny,nx))

                if graph[ny][nx] == 1:
                    graph[ny][nx]=0
                    cnt+=1

                visited[ny][nx]=True

    melt_history.append(cnt)
    return cnt


while True:
    visited=[[False]*widths for _ in range(rows)]
    melt_cnt=bfs()

    if melt_cnt==0: # 녹일 수 있는 치즈가 없다면
        print(time)
        print(melt_history[-2])
        break

    time+=1
