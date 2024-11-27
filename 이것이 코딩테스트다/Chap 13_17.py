# 경쟁적 전염

from collections import deque
import sys

n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
# 4가지 이동 방향에 대한 리스트
dr = [1, -1, 0, 0]  # down, up, right, left
dc = [0, 0, 1, -1]




s,x,y=map(int,input().split())

q=[]
for i in range(n):
    for j in range(n):
        if data[i][j]!=0:
            q.append((data[i][j],i,j,s))
q.sort()
queue=deque(q)

def bfs():
    while queue:
        virus,row,col,time=queue.popleft()
        if time <=0:
            break
        for i in range(4):
            r=row+dr[i]
            c=col+dc[i]
            if 0<=r<n and 0<=c<n and data[r][c]==0:
                data[r][c]=virus
                queue.append((virus,r,c,time-1))
    print(data[x-1][y-1])

bfs()
