# 15559번 내 선물을 받아줘
import sys
from collections import deque

n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]

visited=[[0]*m for _ in range(n)]

# 선물의 개수 count
count=0


# 그룹의 개수 group
group=0

def bfs(x,y):
    global group
    
    q=deque()
    q.append((x,y))

    # 방문처리를 group으로 처리 -> 왜 group으로 처리해야하는지 의문
    visited[x][y]=group

    while q:
        x,y=q.popleft()

        # 현재 위치가 s라면 아래로 이동
        if arr[x][y]=='S':
            #아래가 방문한적이 없다면
            if visited[x+1][y]==0:
                # q에 담아주고 다음 위치를 group으로 방문처리
                q.append((x+1,y))
                visited[x+1][y]=group
        
        # 아래로 이동했는데 지금 group보다 작다면
        # 이전에 방문했었다. 즉 하나의 그룹으로 가능하므로 추가 그룹이 없다 
        # 0 반환

            elif visited[x+1][y]<group:
                return 0

        elif arr[x][y]=='E':
            if visited[x][y+1]==0:
                q.append((x,y+1))
                visited[x][y+1]=group
            
            elif visited[x][y+1]<group:
                return 0


        elif arr[x][y] == 'N':
            if visited[x - 1][y] == 0:
                q.append((x - 1, y))
                visited[x - 1][y] = group
            elif visited[x - 1][y] < group:
                return 0

        elif arr[x][y] == 'W':
            if visited[x][y - 1] == 0:
                q.append((x, y - 1))
                visited[x][y - 1] = group
            elif visited[x][y - 1] < group:
                return 0

        # 다 했는데도 기존 그룹이 없다면 새로운 그룹이므로
        # 1반환
        
    return 1


for i in range(n):
    for j in range(m):
        # 방문한적이 없으면
        if visited[i][j]==0:
            # 그룹 1 추가
            group+=1
            # bfs의 결과를 count에 추가
            count+=bfs(i,j)


print(count)
