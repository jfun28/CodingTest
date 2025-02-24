from collections import deque
n=int(input())

dp=[]

for _ in range(n):
    dp.append(list(map(int,input().split())))


for i in range(1,n): # 두번째 집 부터 생각한다. 
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+dp[i][0] 
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+dp[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+dp[i][2]


print(min(dp[n-1]))