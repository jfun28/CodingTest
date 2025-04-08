from itertools import combinations,permutations

def is_prime(n): # n의 2제곱근 까지 순차 탐색하면서 나눠지는게 있나 확인
    # 2 미만의 수는 소수가 아님
    if n < 2:
        return False
    
    # 2부터 n의 제곱근까지 확인
    for i in range(2, int(n**0.5) + 1):
        # 나누어 떨어지면 소수가 아님
        if n % i == 0:
            return False
    
    # 나누어 떨어지는 수가 없으면 소수
    return True

def solution(numbers):
    num_list=[]
    answer=0
    make_num=[]
    for i in numbers:
        num_list.append(int(i))
    
    for i in range(1,len(num_list)+1):
        for comb in permutations(num_list,i):
            print(comb)
            comb_int=int(''.join(map(str, comb)))
            if not comb_int in make_num:
                make_num.append(comb_int)
                if is_prime(comb_int):
                    answer+=1
    return answer


numbers=['17','011']

for num in numbers:
    solution(num)