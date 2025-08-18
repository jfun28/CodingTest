import sys
from itertools import combinations

input=sys.stdin.readline

def dfs_search(li):
    global answer
    visited=[] # 꽃잎이 서로 닿지 않는지 확인
    total=0 # 꽃을 피울 때 해당 좌표의 대여 비용을 합할 변수

    for r,c in li:
        visited.append((r,c)) # 꽃의 중앙 좌표를 먼저 담는다
        total+=graph[r][c]
        for idx in range(4):
            nr=r+d[idx][0]
            nc=c+d[idx][1]

            if (nr,nc) not in visited:
                visited.append((nr,nc))
                total+=graph[nr][nc]
            else: # 날개가 닿을 경우 함수를 종료한다.
                 return

    answer=min(answer,total)

n=int(input())

d=[(-1,0),(1,0),(0,-1),(0,1)]

graph=[]
answer=int(1e9)
for _ in range(n):
    graph.append(list(map(int,input().split())))

candidated=[(r,c) for r in range(1,n-1) for c in range(1,n-1)]

for li in combinations(candidated,3):
    dfs_search(li)

print(answer)