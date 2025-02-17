import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x,y,h): # 받아야 되는것 x,y 위치와 h 높이 임계값
    visited[x][y]=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n and 0<=ny<n):
            # 방문한적이 없고 h보다 크면 다시 한번 dfs
            if visited[nx][ny]==0 and graph[nx][ny]>h:
                dfs(nx,ny,h)



n=int(input())
graph=[]
maxNum=0
for i in range(n):
    graph.append(list(map(int, input().split()))) # 여기서는 그래프를 입력받고

# 2차원 리스트 최솟값, 최댓값
min_h=min(map(min,graph))
max_h=max(map(max,graph))

safe_area_num=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]


for h in range(min_h-1,max_h):
    visited=[[0]*n for i in range(n)]
    safe_area_num=0
    for i in range(n):
        for j in range(n):
            # 방문한 적이 없고 기준 높이 보다 크면 -> 물에 잠기지 않은 범위 계산
            if (visited[i][j]==0 and graph[i][j]>h):
                dfs(i,j,h)
                safe_area_num+=1
    
    if maxNum<safe_area_num:
        maxNum=safe_area_num

print(maxNum)

