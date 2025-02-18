from collections import deque
import sys
input=sys.stdin.readline
INF=sys.maxsize


def bfs(num):
    global ans
    que=deque()
    que.append(num)
    dp[num]=0
    while que:
        now=que.popleft()
        if now==n-1:
            ans=min(ans,dp[n-1])
        else:
            for i in range(1,A[now]+1):
                if now+i<n and dp[now+i] > dp[now]+1: # n을 초과하지 않고 dp[now+i]가 이전 꺼에서 1 더한 상태보다 많이 나올때 교체
                    dp[now+i]=dp[now]+1
                    que.append(now+i)


n=int(input())

A=list(map(int,input().split()))
dp=[INF]*(n)
ans=INF
bfs(0)

print(ans if ans!=INF else -1)