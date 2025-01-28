n=int(input())
dp=[1]*n
soldier=list(map(int,input().split()))

for i in range(1,n):
    for j in range(0,i):
        if soldier[j]>soldier[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(dp)            
print(n-max(dp))