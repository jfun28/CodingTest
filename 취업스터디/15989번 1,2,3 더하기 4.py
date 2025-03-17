count = int(input())

for _ in range(count):
    n = int(input())
    dp = [0] * (n + 1)
    
    if n < 5:
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
        elif n == 3:
            print(3)
        elif n == 4:
            print(4)
    else:
        dp[2] = 1
        dp[3] = 3
        dp[4] = 4
        dp[5] = 5
        
        for i in range(5, n + 1):
            # 점화식
            dp[i] = 1 + dp[i-2] + i//3
            
        print(dp[n])