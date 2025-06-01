
word=input()

#펠린드롬인지 체크
def check_palindrome(word):
    count=0
    n=len(word)
    if n==1:
        return -1
    # 전부 같은 문자열인지 확인하기
    if n==word.count(word[0]):
        return -1
    
    # 팰린드롬인제 확인하기
    left=0
    right=n-1
    flag=True

    while left<right: 
        if word[left]==word[right]:
            left+=1
            right-=1

        else:
            flag = False
            break

    if flag: # 팰린드룸이면 하나 빼서 반환
        return n-1
    else: # 팰린드룸이 아니면 그 자체로 문자열 길이 반환
        return n
    
print(check_palindrome(word))