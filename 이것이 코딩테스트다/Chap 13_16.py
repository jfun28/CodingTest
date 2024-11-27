#연구소
n,m=map(int,input().split())

temp=[[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

data=[list(map(int,input().split())) for _ in range(n)]

# 4가지 이동 방향에 대한 리스트
dx=[-1,0,1,0]
dy=[0,1,0,-1]

result=0
num=0
# 깊이 우선 탐색을 이용해 각 바이러스가 사방으로 퍼지도록 하기

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)


def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1

    return score


def dfs(count):
    global result
    global num
    # 울타리가 3개가 설치된 경우
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result,get_score())
        num+=1
        return    

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)
print(num)
























#------시간 오버---------
# from collections import deque
# import sys
# import copy

# n,m=map(int,input().split())

# graph=[list(map(int,input().split())) for _ in range(n)]

# result=0
# d=[[-1,0],[1,0],[0,-1],[0,1]]

# def bfs():
#     queue=deque()
#     #queue에 2의 위치 전부 append
#     map=copy.deepcopy(graph)
#     for i in range(n):
#         for k in range(m):
#             if map[i][k]==2:
#                 queue.append((i,k))

#     while queue:
#         r,c=queue.popleft()

#         for i in range(4):
#             dr=r+d[i][0]
#             dc=c+d[i][1]

#             if (0<=dr<n) and (0<=dc<m):
#                 if map[dr][dc]==0:
#                     map[dr][dc]=2
#                     queue.append((dr,dc))

#     global result
#     count =0
#     for i in range(n):
#         for k in range(m):
#             if map[i][k]==0:
#                 count+=1

#     result =max(result,count)


# def make_wall(count):
#     if count ==3:
#         bfs()
#         return
#     for i in range(n):
#         for k in range(m):
#             if graph[i][k]==0:
#                 graph[i][k]=1
#                 make_wall(count+1)
#                 graph[i][k]=0


# make_wall(0)
# print(result)
# print(graph)

