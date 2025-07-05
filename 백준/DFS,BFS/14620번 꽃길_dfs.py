'''
1. 꽃을 피울 수 있는 중앙 좌표의 범위는 동일하다 (1~n-1)
2. 따라서 해당, 행과 열에 따른 탐색을 진행한다 
- visited : 꽃을 피운 좌표를 담는 배열
- total: 꽃을 피운 자리의 대여비용 합을 담을 변수

3. 특정 좌표가 방문한적이 없다면 check함수를 통해 인접한 4개의 칸에도 방문한적이 없는지 확인한다.
5개의 칸 모두 방문한적이 있으면 다음 좌표를 탐색하고 만약에 없으면 방문처리 및 대여비용을 누적시켜 진행한다.

dfs 종료 조건은 3개의 꽃을 다 피웠을 때이다. 따라서 visited에는 꽃을 피운 좌표를 담고 있기 때문에 배열 길이가 5*3이 
되면 dfs를 종료한다.
또한, 시간 단축을 위해 dfs 진행 중 대여비용의 눚적이 최소 비용보다 같거나 크면 종료한다.
'''

import sys
input=sys.stdin.readline

def check(i,j,visited):
    for idx in range(4):
        ni=i+d[idx][0]
        nj=j+d[idx][1]
        if (ni,nj) in visited:
            return False
    return True

def dfs(visited,total):
    global answer
    if total >=answer:
        return
    if len(visited)==3*5:
        answer=min(answer,total)

    else:
        for i in range(1,n-1): # 중앙점을 파악하는 코드 
            for j in range(1,n-1):
                if check(i,j,visited) and (i,j) not in visited:
                    temp=[(i,j)]
                    temp_cost=fields[i][j]
                    for idx in range(4):
                        ni=i+d[idx][0]
                        nj=j+d[idx][1]
                        temp.append((ni,nj))
                        temp_cost+=fields[ni][nj]

                    dfs(visited+temp, total+temp_cost)


d=[(-1,0),(1,0),(0,-1),(0,1)]

n=int(input())
answer=int(1e9)
fields=[list(map(int,input().split())) for _ in range(n)]

dfs([],0)

print(answer)
