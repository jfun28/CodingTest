import sys
from collections import deque
input=sys.stdin.readline

# 입력
N,M=map(int,input().split())
pixels=[]
screen=[[] for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    pixels.append(list(map(int,input().split())))

T=int(input())

# 화면값 계산

screen=[[0]*M for _ in range(N)]

for row in range(N):
    for width in range(0,M*3,3):
        if sum(pixels[row][width:width+3])//3>=T:
            screen[row][width//3]=255

# 물체 계산
que=deque()
# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(r,c):
    que.append((r,c))
    visited[r][c]=True
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and screen[nx][ny]==255:
                    visited[nx][ny]=True
                    que.append((nx,ny))


cnt=0
for x in range(N):
    for y in range(M):
        if screen[x][y]==255 and not visited[x][y]:
            bfs(x,y)
            cnt+=1

print(cnt)














# import sys
# from collections import deque
# input=sys.stdin.readline 

# rows, widths=map(int,input().split())

# graph=[]

# for _ in range(rows):
#     graph.append(list(map(int,input().split())))


# threshold=int(input())

# real_pixels=[[0]*widths for _ in range(rows)]
# def calculate_graph(graph):
#     for row in range(rows):
#         for width in range(0,widths*3,3):
#             if sum(graph[row][width:width+3])//3>=threshold:
#                 real_pixels[row][width//3]=255

# dx=[1,-1,0,0]
# dy=[0,0,-1,1]
# visited=[[False]*widths for _ in range(rows)]
# def bfs():
#     q=deque()
#     q.append((0,0))
#     visited[0][0]=True
#     cnt=0
#     while q:
#         y,x=q.popleft()
#         if graph[y][x]==255:

#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]

#             if 0<=nx<widths and 0<=ny<rows and not visited[ny][nx]:
#                 if graph[ny][nx]==255:
#                     if graph[y][x]==255:
#                         graph[ny][nx]=0
#                     else:
#                         cnt+=1

#                     graph[ny][nx]=0
        



# calculate_graph(graph)

# bfs()

# print(real_pixels)