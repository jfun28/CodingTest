# 1010번 다리 놓기

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[1] = [i for i in range(M+1)]  # 초기값
    for n in range(2, N+1):
        for m in range(1, M+1):
            dp[n][m] = sum(dp[n-1][m-i] for i in range(1, m+1))

    print(dp[N][M])



























# n = int(input())
#
# left_river = []
# right_river = []
#
# def my_factorial(n):
#     if(n>1):
#         return n*my_factorial(n-1)
#     else:
#         return 1
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     left_river.append(x)
#     right_river.append(y)
#
# for i in range(n):
#     left=left_river[i]
#     right=right_river[i]
#     result=my_factorial(right)/(my_factorial(right-left)*my_factorial(left))
#     print(int(result))
