def solution(s):
    result=[]

    if len(s)==1:
        return 1
    
    for i in range(1,len(s)+1):
        b=''
        cnt=1
        tmp=s[:i]

        for j in range(i,len(s)+i,i):
            if tmp ==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b=b+str(cnt)+tmp # s[j:i+j]가 아니라 tmp로 해줘야하는 이유는 반복문이 j가 문자열 끝 인덱스 까지 접근 하기 때문에 
                    # 끝을 문자열로 넣으면 빈 값이 들어가 항상 min값은 0이 나오게 된다.  
                else:
                    b=b+tmp
                tmp=s[j:j+i]
                cnt=1  

        result.append(len(b))    
      



    return min(result)

print(solution('aabbaccc'))















































# def solution(s):
#     result=[]
#     if len(s)==1:
#         return 1
    
#     for i in range(1,len(s)+1): # n개씩 늘려가면 탐색하는 반복문
#         b='' # 축약된 문자열을 담을 변수
#         cnt=1 # 묶
#         tmp=s[:i]

#         for j in range(i,len(s)+i,i): # n개 정해지면 한 문자열에 n개씩 잘라서 비교하는 반복문

#             if tmp==s[j:i+j]: # 앞에서 부터 비교하는 문자가 같다면 앞에 표시할 숫자 계속 count
#                 cnt+=1
#             else: # 만약에 다르다면 같은 문자 인식 되는게 끝나는 것이므로 압축되어 표시된 문자 표시
#                 if cnt!=1: 
#                     b=b+str(cnt)+tmp # 반복된 수를 문자로 변화해서 압축된 문자표현식으로 표시해서 b에 담는다. 
#                 else: # 압축된게 없어서 그 문자 하나일경우 그냥 그 문자하나만 b에 담는다.
#                     b=b+tmp
                
#                 tmp=s[j:j+i] # 비교할 문자 앞으로 전진
#                 cnt=1 # count 초기화

#         result.append(len(b))

#     return min(result)




