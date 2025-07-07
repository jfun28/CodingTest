'''
1. 행과 열 인덱스의 하나 이상은 넉넉하게 와야하기 때문에 1~n-1로 범위를 설정함
2. 꽃의 중앙의 위치 정보를 담을 수 있는 리스트 배열이 필요하다


# 알고리즘
1. Candidate리스트로 꽃을 피울 수 있는 모든 좌표 (행,열)들을 배열에 담는다
2. Candidate리스트에서 3개의 좌표를 뽑아 해당 좌표에 꽃을 피웠을 때 모두 피울 수 있는지 확인한다
3. 모든 꽃잎이 서로 닿지 않고 피울 수 있다면 해당 좌표의 대여비용을 모구 합하여 answer 변수에 최소값을 갱신한다
'''

import sys

from itertools import combinations

input=sys.stdin.readline

n=int(input())
graph=[]


for _ in range(n):
    graph.append(list(map(int,input().split())))

candidates=[(r,c) for r in range(1,n-1) for c in range(1,n-1)]


def check(li):
    global answer
    visited=[]
    total=0
    for r,c in li:
        visited.append((r,c))
        total+=graph[r][c]
        for i in range(4):
            nr=r+d[i][0]
            nc=c+d[i][1]
            if (nr,nc) in visited:
                return
            visited.append((nr,nc))
            total+=graph[nr][nc]
    answer=min(answer,total)
    
answer=int(1e9)

d=[(-1,0),(1,0),(0,-1),(0,1)]

for li in combinations(candidates,3):
    check(li)

print(answer)