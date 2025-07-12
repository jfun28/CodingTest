import sys
from copy import deepcopy
input=sys.stdin.readline

T=int(input())


for _ in range(T):
    n,d=map(int,input().split())
    graph=[]

    for _ in range(n):
        graph.append(list(map(int,input().split())))

    ans=[[0]*n for _ in range(n)]
    if d<0:
        d+=360

    if d==360 or d==0:
        for i in graph:
            print(*i)
    
    else:
        mid=n//2
        for _ in range(d//45):
            for i in range(n):
                for j in range(n):
                    
                    # 가운데 행 -> 주 대각선
                    if i==j:
                        ans[i][j]=graph[mid][j]
                    
                    # 주대각선 -> 가운데열
                    elif j==mid:
                        ans[i][j]=graph[i][i]

                    # 부대각선->가운데 행
                    elif i==mid:
                        ans[i][j]=graph[i][n-i-1]

                    # 가운데 열-> 부대각선
                    elif i+j==n-1:
                        ans[i][j]=graph[i][mid]

                    else:
                        ans[i][j]=graph[i][j]

            graph=deepcopy(ans)
        for k in graph:
            print(*k)

    









