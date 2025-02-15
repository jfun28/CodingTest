import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x,y,h): # 받아야 되는것 x,y 위치와 h 높이 임계값
    visted[x][y]=1

    f







n=int(input)
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
    

