import sys
import math

def is_perfect_square(n):
    """완전제곱수인지 빠르게 판별"""
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def solve():
    M, N = map(int, sys.stdin.readline().split())
    
    # 입력을 더 간단하게 처리
    grid = []
    for _ in range(M):
        line = sys.stdin.readline().strip()
        grid.append([int(ch) for ch in line])
    
    max_result = -1
    
    # 모든 시작점에 대해
    for start_row in range(M):
        for start_col in range(N):
            # 모든 가능한 공차에 대해
            for dr in range(-M, M):
                for dc in range(-N, N):
                    # 한 자리수도 고려해야 하므로 (0,0) 제외하지 않음
                    
                    r, c = start_row, start_col
                    current_number = ""
                    
                    # 격자 범위 내에서 등차수열 생성
                    while 0 <= r < M and 0 <= c < N:
                        current_number += str(grid[r][c])
                        
                        # 현재까지 만든 수가 완전제곱수인지 확인
                        num = int(current_number)
                        if is_perfect_square(num):
                            max_result = max(max_result, num)
                        
                        # 공차가 (0,0)이면 한 자리수만 확인하고 종료
                        if dr == 0 and dc == 0:
                            break
                            
                        # 다음 위치로 이동
                        r += dr
                        c += dc
    
    print(max_result)

solve()