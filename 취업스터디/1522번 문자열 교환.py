def min_swaps_continuos(s):
    # 문자열의 길이
    n=len(s)

    # a의 총 개수 (윈도우 크기)
    count_a=s.count('a')

    # a가 없거나 모든 문자가 a인 경우
    if count_a==0 or count_a==n:
        return 0
    
    # 원형 문자열을 처리하기 위해 문자열을 2배로 확장
    s=s+s

    min_swaps=float('inf')

    # 모든 가능한 시작 위치에 대해 검사
    for i in range(n):
        # 현재 윈도우에서 b의 개수 (교환이 필요한 개수)
        window=s[i:i+count_a]
        swap_need=window.count('b')

        min_swaps=min(min_swaps,swap_need)

        return min_swaps

s=input()
print(min_swaps_continuos(s))
