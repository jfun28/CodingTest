import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())


graph = []  # 2차원 배열 생성
for i in range(n):
    row = list(map(int, input().split()))  # 한 행의 값들을 입력받기
    graph.append(row)  # gra

dx=[-1,1,0,0]
dy=[0,0,-1,1]
picture_size = []  # 동적 리스트로 변경


def dfs(x,y,index):
    graph[y][x] = 0  # 현재 칸 방문 처리
    size = 1 
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<m) and (0<=ny<n) and graph[ny][nx]==1:
            size += dfs(nx,ny,index)  # 반환된 크기를 더함
    return size

picture_num=0

for i in range(m): # x축(열) 
    for j in range(n): # x축(행)
        if graph[j][i]==1: # 이차원 배열에서는 [행][열]
            size = dfs(i,j,picture_num)
            picture_size.append(size)
            picture_num+=1


print(picture_num)
print(max(picture_size) if picture_size else 0)  # 그림이