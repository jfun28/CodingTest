import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[]

for _ in range(m):
    graph.append(list(map(str,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


W_army_size = []  # 동적 리스트로 변경
B_army_size=[]

def dfs(x,y,cnt,discret):
    graph[y][x] = 0  # 현재 칸 방문 처리

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if  (0 <= ny < m) and (0 <=nx < n) and graph[ny][nx]==discret:
            cnt= dfs(nx,ny,cnt+1,discret)  # 반환된 크기를 더함

    return cnt


W_index_num=0
B_index_num=0

for i in range(m): #y축(행) 
    for j in range(n): # x축(열)
        if(graph[i][j] == 'W'):
            W_index_num += (dfs(j, i, 1, 'W'))**2
        elif(graph[i][j] == 'B'):
            B_index_num += (dfs(j, i, 1, 'B'))**2


print(W_index_num,B_index_num)




