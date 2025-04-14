import sys
from itertools import combinations
n = sys.stdin.readline().strip()
min_value = int(1e9)
max_value = 0

# 한자리 숫자일 때
def check_odd(n):
    # 1. 각 자리 숫자 중 홀수의 개수를 적는다.
    temp = 0
    for i in n:
        if int(i) % 2 == 1:
            temp += 1
    return temp

# n is string
def solve(n, count):
    global min_value, max_value

    if len(n) == 1: # 2. 수가 한자리 , then 종료
        min_value = min(count, min_value)
        max_value = max(count, max_value)
        return

    elif len(n) == 2: # 3. 두자리 수 는 2개로 나눠서 합 , 새로운 수 생성
        new = str(int(n[0]) + int(n[1])) # 새로운 수 생성 
        return solve(str(new), count+check_odd(new)) # 재귀 호출, 새로운 숫

    else:
        new_num=0
        index_list=[i for i in range(1,len(n))]
        for index_comb in combinations(index_list,2):
            first = n[:index_comb[0]]
            second = n[index_comb[0]:index_comb[1]]
            third = n[index_comb[1]:]
            new_num = str(int(first) + int(second) + int(third)) # 새로운 숫자 만들기
            solve(new_num, count+check_odd(new_num)) # 새로운 숫자에 있는 홀수 개수 카운트를 누적해서 더함.

x = check_odd(n)
solve(n, x)
print(min_value, max_value)


    



