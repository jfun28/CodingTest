
'''
백트래킹으로 풀면 런타임에러 난다 => BFS로 풀어야한다.
여기서 굳이 min 활용해서 경로의 최솟값을 구하지 않아도 되는 이유로는 bfs로 하면서 가장 가까운 거리에 있는 경로가 먼저 visited 처리 되기 때문에
짧은거리만 count 된다.

'''
from collections import deque

def solution(maps):
    n,m=len(maps), len(maps[0])

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    queue=deque([(0,0,1)])
    visited=[[False]*m for _ in range(n)]
    visited[0][0]=True

    while queue:
        x,y, dist=queue.popleft()

        if x==n-1 and y==m-1:
            return dist
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append([nx,ny,dist+1])


    return -1






# import sys
# sys.setrecursionlimit(1001)

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
    
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     ans = []  # 함수 내부로 이동
#     visited = [[False] * m for _ in range(n)]  # 함수 내부로 이동
    
#     def dfs(x, y, count):
#         if x == n-1 and y == m-1:
#             ans.append(count)
#             return                
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위 수정
#                 continue  
#             if maps[nx][ny] == 1 and visited[nx][ny] == False:
#                 visited[nx][ny] = True
#                 dfs(nx, ny, count + 1)
#                 visited[nx][ny] = False
    
#     visited[0][0] = True
#     dfs(0, 0, 1)
    
#     if len(ans) > 0:             
#         answer = min(ans)
#     else:
#         answer = -1
   
#     return answer