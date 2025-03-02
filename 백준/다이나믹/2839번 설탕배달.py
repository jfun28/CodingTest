n=int(input())

dp=[-1]*(n+1)

if n<3 or n==4:
    print(-1)

elif n==3 or n==5:
    print(1)

else:   
    dp[3]=dp[5]=1
    for i in range(6,n+1):
        if i%5==0:
            dp[i]=dp[i-5]+1
        elif i%3==0:
            dp[i]=dp[i-3]+1

        else:
            dp[i]=min(dp[i-5],dp[i-3])+1


    print(dp[n])