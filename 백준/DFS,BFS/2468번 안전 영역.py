import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x,y,h): # 받아야 되는것 x,y 위치와 h 높이 임계값->이 과정을 통해 전체 붙어 있는 면적을 구한다. 
    visited[x][y]=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n) and (0<=ny<n):
            # 방문한적이 없고 기준 높이보다 크면 다시 한번 dfs
            if visited[nx][ny]==0 and graph[nx][ny]>h:
                visited[x][y]=1
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
max_safe = 0  # 최대 안전 영역 수

for h in range(min_h-1,max_h):
    visited=[[0]*(n) for _ in range(n)]
    safe=0 # 안전한 영역 개수
    for i in range(n):
        for j in range(n):
            # 방문한적이 없고 기준 높이 보다 크면-> 물에 잠기지 않은 범위 계산 
            if(visited[i][j]==0 and graph[i][j]>h):
                dfs(i,j,h)
                safe+=1 # 안전 영역 갯수 추가
    
    if (safe>max_safe): max_safe=safe
    
print(max_safe)

