import sys
input=sys.stdin.readline
from itertools import combinations

noodle,wok=map(int,input().split())
wokSize=list(map(int,input().split()))

# 양손잡이가 한 번의 요리를 만들 수 있는 모든 noodle 개수 집합

wokCombi=set(wokSize)
combi=combinations(wokSize,2)
for j in combi:
    wokCombi.add(sum(j))

    
dp=[0]*(noodle+1)
# wokCombi에서 몇번을 더해야 noodle 개수가 될지 동적계획법
if noodle in wokCombi:
    print(1)

else:
    for i in range(1,len(dp)):
        minval=float("inf")
        for x in wokCombi:
            if (i-x>=0):
                minval=min(minval,dp[i-x]+1)
        
        dp[i]=minval
    
    print(-1 if dp[-1]==float('inf') else dp[-1])


    