import sys
input=sys.stdin.readline

n=int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs=[0]*301

for i in range(1,n+1):
    stairs[i]=int(input())

# dp 배열을 초기화합니다. 
dp=[0]*301

dp[1]=stairs[1]
dp[2]=stairs[1]+stairs[2]
dp[3]=max(stairs[1]+stairs[3],stairs[2]+stairs[3])

# 점화식을 계산한다.
for i in range(4,n+1):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    # dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i],dp[i-3]+stairs[i-2]+stairs[i]) 얼핏 생각하면 이것도 될 수 있겠지만 두 번째 조건하고 겹친다.

print(dp[n])