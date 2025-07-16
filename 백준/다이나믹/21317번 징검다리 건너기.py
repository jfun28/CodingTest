# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [int(1e9)] * n
# dp[0] = 0  # 시작점의 비용은 0
# rock_power = []

# for _ in range(n-1):
#     small_jump, big_jump = map(int, input().split())
#     rock_power.append((small_jump, big_jump))

# k = int(input())

# for i in range(n-1):  
        
#     # 작은 점프 (1칸)
#     if i + 1 < n:
#         dp[i + 1] = min(rock_power[i][0] + dp[i], dp[i + 1])
    
#     # 큰 점프 (2칸)
#     if i + 2 < n:
#         dp[i + 2] = min(rock_power[i][1] + dp[i], dp[i + 2])
    
#     # 특수 점프 (3칸, 비용 k)
#     if i + 3 < n:
#         dp[i + 3] = min(k + dp[i], dp[i + 3])

# print(dp[n-1])

import sys
input = sys.stdin.readline

n = int(input())

# dp[i][0]: 매우 큰 점프를 사용하지 않고 i번째 돌에 도달하는 최소 비용
# dp[i][1]: 매우 큰 점프를 한 번 사용하여 i번째 돌에 도달하는 최소 비용
dp = [[int(1e9)] * 2 for _ in range(n)]
dp[0][0] = 0  # 시작점
dp[0][1] = 0  # 시작점에서는 매우 큰 점프 사용 여부와 상관없이 0

rock_power = []
for _ in range(n-1):
    small_jump, big_jump = map(int, input().split())
    rock_power.append((small_jump, big_jump))

k = int(input())

for i in range(n-1):
    # 작은 점프 (1칸)
    if i + 1 < n:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + rock_power[i][0])
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + rock_power[i][0])
    
    # 큰 점프 (2칸)
    if i + 2 < n:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + rock_power[i][1])
        dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + rock_power[i][1])
    
    # 매우 큰 점프 (3칸, 한 번만 사용 가능)
    if i + 3 < n:
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)  # 매우 큰 점프를 아직 사용하지 않은 상태 (dp[i][0])에서만 매우 큰 점프를 사용할 수 있음
                                                        # 이미 매우 큰 점프를 사용한 상태(dp[i][1])에서는 매우 큰 점프를 사용할 수 없음
print(min(dp[n-1][0], dp[n-1][1])) 