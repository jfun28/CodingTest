from collections import deque
import sys

input=sys.stdin.readline
n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0] * (n + 1)
max_p = 0

# 날짜별로 DP 배열 업데이트
for i in range(n):
    # 이전까지의 최대 이익 반영
    dp[i] = max(dp[i], max_p)
    
    # 현재 상담을 선택하는 경우
    T, P = schedule[i]
    if i + T <= n:  # 상담이 기간 내에 끝나는 경우
        dp[i + T] = max(dp[i + T], dp[i] + P)
    
    # 현재까지의 최대 이익 갱신
    max_p = max(max_p, dp[i])

# 마지막 날까지의 최대 이익
print(max(max_p, dp[n]))
