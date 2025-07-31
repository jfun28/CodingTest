import sys
from copy import deepcopy
input=sys.stdin.readline

T=int(input())


for _ in range(T):
    n,d=map(int,input().split())
    graph=[]
    ans=[[0]*n for i in range(n)]
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    if d<0:
        d+=360
        
    if d==360 or d==0:
        for i in graph:
            print(*i)
    
    else:

        for _  in range(d//45):
            mid=n//2


            for i in range(n):
                for j in range(n):
                    # 1. 주대각선=>가운데 열
                    if mid==j :
                        ans[i][j]=graph[i][i]
                    
                    # 2. 가운데 열 -> 부 대각선 
                    elif (n-1-i)==j:
                        ans[i][j]=graph[i][mid]

                    # 3. 부 대각선 -> 가운데 행
                    elif mid==i:
                        ans[i][j]=graph[n-j-1][j]

                    # 4. 가운데 행 -> 주 대각선
                    elif i==j:
                        ans[i][j]=graph[mid][j]

                    else:
                        ans[i][j]=graph[i][j] 

            graph=deepcopy(ans)

        for i in graph:
            print(*i)
    
                    
