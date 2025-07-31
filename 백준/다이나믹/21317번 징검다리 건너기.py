import sys
input=sys.stdin.readline

n=int(input())
dp=[[int(1e9)]*2 for _ in range(n)]
dp[0][0]=0 # 시작점에서는 매우 큰 점프를 사용 여부와 상관없이 0에서 시작
dp[0][1]=0
rock_power=[]

for _ in range(n-1):
    small_jump,big_jump=map(int,input().split())
    rock_power.append((small_jump,big_jump))

k=int(input())

for i in range(n-1):
    
    if i<=n-2:
        dp[i+1][0]=min(dp[i+1][0],dp[i][0]+rock_power[i][0]) # 여기는 한칸 움직이고
        dp[i+1][1]=min(dp[i+1][1],dp[i][1]+rock_power[i][0])
    if i<=n-3:    
        dp[i+2][0]=min(dp[i+2][0],dp[i][0]+rock_power[i][1]) # 여기는 두칸 움직이고
        dp[i+2][1]=min(dp[i+2][1],dp[i][1]+rock_power[i][1])
    if i<=n-4: # 매우 큰 점프 사용 
        dp[i+3][1]=min(dp[i+3][1],dp[i][0]+k)


print(min(dp[-1]))