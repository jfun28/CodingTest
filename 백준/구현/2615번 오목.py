import sys
input=sys.stdin.readline

'''
- 출력해야하는 제일 왼쪽 좌표를 기준으로 주 대각선, 세로줄, 가로줄, 부 대각선 순으로 하여 4개의 방향을 탐색
- 단, 조건으로 6개 연속인 바둑알은 승리가 아니므로, 연속된 조건의 count를 자신을 제외하고 각 방향으로 5번 까지만 진행한 후 연속된 바둑알의
갯수가 4개인 경우만 승리로 간주한다
'''

n=19

blacks=[]
whites=[]
board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            blacks.append((i,j))

        elif board[i][j]==2:
            whites.append((i,j))

def search(omoks):
    dx = [1, 1, 0, -1]
    dy = [1, 0, 1, 1]

    for x,y in omoks:
        for i in range(4):
            cnt=0
            for k in range(1,6): # 대각선을 다루는 방법
                nx=x+dx[i]*k
                ny=y+dy[i]*k

                if nx<0 or nx>=n or ny <0 or ny>=n:
                    continue
                if (nx,ny) not in omoks:
                    break
                if (nx,ny) in omoks:
                    cnt+=1

            tx=x-dx[i] # 시작점의 반대 한칸 옆에도 돌이 있는가 체크
            ty=y-dy[i]

            if (tx,ty) not in omoks and cnt ==4:
                return (x+1,y+1)
            
    return False


black_result=search(blacks)
white_result=search(whites)

if black_result:
    print(1)
    print(*black_result)

elif white_result:
    print(2)
    print(*white_result)

else:
    print(0)
