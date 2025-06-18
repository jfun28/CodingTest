import sys
from collections import deque
input=sys.stdin.readline


def bfs(x,y,dst_x,dst_y,time):
    q=deque([(x,y,time)])
    visited=[[0]*m for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        x,y,time=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and not visited[nx][ny]:
                if nx==dst_x and ny==dst_y:
                    return time+1
                visited[nx][ny]=1
                q.append((nx,ny,time+1))

    return float('inf') # 만약 도달하지 못한다면 inf 값 반환



n,m,t=map(int,input().split())

graph=[[]*m for i in range(n)]

for i in range(n):
    graph[i]=list(map(int,input().split()))
    if 2 in graph[i]:
        knife=[i,graph[i].index(2)] # 2가 들어있는 행과 열 저장


# 칼 사용 X
not_use_knife=bfs(0,0,n-1,m-1,0) 


# 칼 사용 O
tmp=bfs(0,0, knife[0],knife[1],0)

if tmp!=float('inf'): # 칼 사용할때만 최단 거리이고 칼 사용했을 최종목적지에 도달 못할 수도 있으니 if 문을 통해 선별
    use_knife=tmp+abs(n-1-knife[0])+abs(m-1-knife[1])

else:
    use_knife=tmp

answer=min(not_use_knife, use_knife)

print(answer if answer<t else 'Fail') 
























# import sys
# from collections import deque
# input=sys.stdin.readline

# def bfs(x,y,dst_x,dst_y,time):
#     q=deque([(x,y,time)])
#     visited=[[0]*m for _ in range(n)]
#     dx=[-1,1,0,0]
#     dy=[0,0,-1,1]

#     while q:
#         x,y,time=q.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and not visited[nx][ny]:
#                 if nx==dst_x and ny==dst_y:
#                     return time+1
#                 visited[nx][ny]=1
#                 q.append((nx,ny,time+1))

#     return float('inf')


# n,m,t=map(int,input().split())
# graph=[[] for _ in range(n)]

# for i in range(n):
#     graph[i]=list(map(int,input().split()))
#     if 2 in graph[i]:
#         knife=[i,graph[i].index(2)] # 행과 열 좌표를 리스트로 저장

# # 칼 사용 X
# not_use_knife=bfs(0,0,n-1,m-1,0)

# # 칼 사용 O
# tmp=bfs(0,0, knife[0],knife[1],0)

# if tmp!=float('inf'):
#     use_knife=tmp+abs(n-1-knife[0])+abs(m-1-knife[1])

# else:
#     use_knife=tmp


# ans=min(not_use_knife,use_knife)

# print(ans if ans<=t else 'Fail')

















# # from sys import stdin
# # import sys
# # sys.setrecursionlimit(1000000)

# # input = stdin.readline

# # dr = (-1, 1, 0, 0)
# # dc = (0, 0, -1, 1)

# # def dfs(r, c, visited, steps, has_gram):
# #     global min_time
    
# #     # 목적지에 도달한 경우
# #     if (r, c) == (N-1, M-1):
# #         min_time = min(min_time, steps)
# #         return
    
# #     # 현재 시간이 이미 찾은 최소 시간보다 크거나 같으면 가지치기
# #     if steps >= min_time:
# #         return
    
# #     # 그람을 가지고 있다면 목적지까지 직선거리로 갈 수 있음
# #     if has_gram:
# #         manhattan_dist = abs(N-1-r) + abs(M-1-c)
# #         min_time = min(min_time, steps + manhattan_dist)
# #         return
    
# #     # 4방향 탐색
# #     for d in range(4):
# #         nr = r + dr[d]
# #         nc = c + dc[d]
        
# #         # 격자 밖이면 건너뛰기
# #         if not (0 <= nr < N and 0 <= nc < M):
# #             continue
            
# #         # 벽이거나 이미 방문했다면 건너뛰기
# #         if A[nr][nc] == 1 or visited[nr][nc]:
# #             continue
        
# #         # 방문 표시
# #         visited[nr][nc] = True
        
# #         # 그람을 찾은 경우
# #         if A[nr][nc] == 2:
# #             dfs(nr, nc, visited, steps + 1, True)
# #         else:
# #             dfs(nr, nc, visited, steps + 1, has_gram)
        
# #         # 백트래킹
# #         visited[nr][nc] = False

# # def solve():
# #     global min_time
# #     min_time = T + 1  # 초기값을 T+1로 설정 (실패 케이스)
    
# #     visited = [[False] * M for _ in range(N)]
# #     visited[0][0] = True
    
# #     # 시작점이 그람인 경우 체크
# #     if A[0][0] == 2:
# #         dfs(0, 0, visited, 0, True)
# #     else:
# #         dfs(0, 0, visited, 0, False)
    
# #     return min_time

# # # main
# # N, M, T = map(int, input().split())
# # A = [list(map(int, input().split())) for _ in range(N)]

# # result = solve()

# # if result <= T:
# #     print(result)
# # else:
# #     print("Fail")