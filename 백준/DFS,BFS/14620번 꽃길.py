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

def check(li):
    global answer
    visited=[] # 꽃잎이 서로 닿지 않는지 확인
    total=0 # 꽃을 피울 때 해당 좌표의 대여비용을 힙할 변수
    for r,c in li:
        visited.append((r,c)) # 꽃의 중앙 좌표를 먼저 담는다 
        total+=fields[r][c] # 일단 중앙에 값을 넣어둔다
        for idx in range(4): # 중앙을 기준으로 상하좌우를 확인한다
            nr=r+d[idx][0]
            nc=c+d[idx][1]
            if (nr,nc) not in visited:
                visited.append((nr,nc))
                total+=fields[nr][nc]
            else: # 꽃잎이 서로 닿게되는 경우는 함수를 종료한다.
                return
            
    answer=min(answer, total) # 모든 꽃을 피울 수 있가면 최소 비용으로 최신화한다
    

d=[(-1,0),(1,0),(0,1),(0,-1)]

n=int(input())

answer=int(1e9)

fields=[list(map(int,input().split())) for _ in range(n)]
candidates=[(r,c) for r in range(1,n-1) for c in range(1,n-1)]

for li in combinations(candidates,3):
    check(li)

print(answer)


