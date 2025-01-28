'''1. 어떤 싱태여야지 크로스 했다는 것을 알 수 있을까
   2.           '''

n=int(input())

lists=[]
dp=[1]*n

for i in range(n):
    a,b=map(int,input().split())
    lists.append([a,b])

lists.sort()

print(lists)

for i in range(1,n):
    for j in range(0,i):
        if lists[j][1]<lists[i][1]:
            print(f"i:{i}, j:{j} "+f"lists[j][1]는 {lists[j][1]}이고 lists[i][1]은 {lists[i][1]}")
            dp[i]=max(dp[i],dp[j]+1)

print(dp)
print(n-max(dp))


    