import sys
from collections import deque
input=sys.stdin.readline


n,m=map(int,input().split())


graph=[list(map(int,input().split())) for i in range(m)]

queue=deque([])


dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 어디에 토마토가 있는지 체크
for x in range(n):
    for y in range(m):
        if graph[y][x]==1:
            queue.append([y,x])
            print(queue)


def bfs():
    while queue:
        y,x=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[ny][nx]==0:
                graph[ny][nx]=graph[y][x]+1
                queue.append([ny,nx])



bfs()
answer=0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)

    answer=max(answer,max(i))

print(answer-1)

























# import sys
# input=sys.stdin.readline
# from collections import deque

# def bfs():
#     while queue:
#         # 처음 토마토가 들어있는 좌표를 꺼낸다
#         y,x=queue.popleft()
#         # 처음 토마토 주위 사분면의 익힐 방면을 찾아본다.
#         for i in range(4):
#             nx,ny=x+dx[i],y+dy[i]
#             # 해당 하는 좌표가 좌표 범위 내에서만 움직여야 하고 토마토는 익지 않은 상태(0)이 있어야한다.
#             if 0<=nx<n and 0<=ny<m and graph[ny][nx]==0:
#                 graph[ny][nx]=graph[y][x]+1
#                 queue.append([ny,nx])


# n,m=map(int,input().split())

# graph=[]
# visited=[]
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# for i in range(m):
#     graph.append(list(map(int,input().split())))

# queue=deque([])

# # 처음 queue에 토마토가 있는 x,y의 좌표를 추출해서 넣는다.

# for i in range(n):
#     for j in range(m):
#         if graph[j][i]==1: # 여기 있는 위치 그대로 받는 거기 떄문에 x와 y를 바꿔서 넣어야 한다
#             queue.append([j,i]) # queue에다가 넣을때는 이차원리스트에 넣는 것 처럼 [y][x]를 바꾸어 넣는다.

# # bfs함수는. 한번 들어가면 무조건 다 돌고 나오니깐 재귀 할 필요 없음

# print(graph)
# bfs()
# day=0
# for i in graph:
#     for j in i:
#         if j==0:
#             print(-1)
#             exit(0)

#     day=max(day,max(i))

# print(day-1) # 초반에 원래 들어 있는 토마토 1을 했으니 1을 뺴준다(내가 구하고 싶은것은 걸린 날짜)

