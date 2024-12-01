# #팰린드롬: 앞에서 읽을때와 뒤에서 읽을 때랑 같은거

from collections import Counter

def make_palindrome(name):
    # 각 문자의 출현 횟수를 세기
    char_count = Counter(name)
    
    # 홀수 개 있는 문자 확인
    odd_chars = [char for char, count in char_count.items() if count % 2 == 1]
    
    # 홀수 개 있는 문자가 2개 이상이면 팰린드롬 불가능
    if len(odd_chars) > 1:
        return "I'm Sorry Hansoo"
    
    # 팰린드롬 만들기
    result = []
    mid = ""
    
    # 알파벳 순으로 정렬
    for char in sorted(char_count.keys()):
        # 해당 문자의 개수
        count = char_count[char]
        
        # 짝수 개인 경우
        result.append(char * (count // 2))
        
        # 홀수 개인 경우 가운데 문자로 저장
        if count % 2 == 1:
            mid = char
    
    # 왼쪽 부분
    left = "".join(result)
    # 오른쪽 부분 (왼쪽 부분을 뒤집은 것)
    right = left[::-1]
    
    # 최종 팰린드롬 만들기
    return left + mid + right

# 입력 받기
name = input()
# 결과 출력
print(make_palindrome(name))
















# from collections import deque

# m=list(input())

# m.sort()

# m=deque(m)
# print(m)
# palindrome_left=deque()
# palindrome_right=deque()

# def judge_palindrome(palindrome):
#     result = ''.join(palindrome)
#     end_index=round(len(palindrome)/2)
#     if palindrome[:end_index]==palindrome[end_index:]:
#         print(result)
#     else:
#         print("I'm Sorry Hansoo")
#         print(result)

# def make_palindrome(m):
  
#     while len(m)!=0:
        
#         if len(m)>=2:
#             start=m.popleft()
#             end=m.popleft()
#             print("start",start)
#             print("end",end)

#             if start==end:
#                 palindrome_left.append(start)
#                 palindrome_right.appendleft(end)

#             elif start!=end :
#                 m.appendleft(end)
#                 m.append(start)
#             else:
#                 start=m.popleft()
#                 palindrome_left.append(start)

      
#         else:
#             start=m.popleft()
#             palindrome_left.append(start)


    
#         palindrome=palindrome_left+palindrome_right
#     return palindrome



# palindrome=list(make_palindrome(m))

# judge_palindrome(palindrome)