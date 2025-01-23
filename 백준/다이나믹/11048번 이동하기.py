n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+graph[i][j]
        
print(dp[n-1][m-1])

# 여기서도 특유의 다이나믹 프로그래밍 문제 처럼 어떠한 것을 기준으로 그 직전에 상황
#들을 고려하여 점화식을 세워 접근하였다. 