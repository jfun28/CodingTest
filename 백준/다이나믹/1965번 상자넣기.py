n=int(input())

box=list(map(int,input().split()))

dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if box[i]>box[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))


# 기준점을 정하고 차례대로 훑으면서 비교를 하고 dp 배열을 업데이트 하는 방식
