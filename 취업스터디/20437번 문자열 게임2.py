from collections import defaultdict
n=int(input())

def find_answer(s_line):
    
    alpha_dict=defaultdict(list)
        
    # 결과가 없을 경우 -1로 설정
    min_length = int(10**6)  # 문제 1: 최소 길이
    max_length = 0            # 문제 2: 최대 길이

    for i in range(len(s_line)):  # 이것은 끝과 끝을 구하는 것  
        if s_line.count(s_line[i])>=k:
            alpha_dict[s_line[i]].append(i)
            
    # k개 이상 존재하는 알파벳이 없는 경우
    if not alpha_dict:
        return -1,
        
    # 해당문자를 k개 포함하는 문자열 길이를 구하기
    for idx_list in alpha_dict.values(): # k넘는 알파벳 하나하나 호출하면서 구하기
        for j in range(len(idx_list)-k+1): # 이게 연속해서 나올수 있는 윈도우의 길이가 됨
            alpha_len=idx_list[j+k-1]-idx_list[j]+1 # 어차피 가장 짧을 때랑 가장 길때의 상황은 구하고자 하는 알파벳이 양 끝에 와야지 성립이 된다. 
            max_length=max(max_length,alpha_len)
            min_length=min(min_length,alpha_len)

    return min_length,max_length

for _ in range(n):
    s_line=input().strip()
    k=int(input())        
    print(*find_answer(s_line))
