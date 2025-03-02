n=int(input())
line=[]
for _ in range(n):
    a,b=map(int,input().split())
    line.append((a,b))

line.sort()
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if line[j][1]<line[i][1]:
            dp[i]=max(dp[i],dp[j]+1)


print(n-max(dp))
