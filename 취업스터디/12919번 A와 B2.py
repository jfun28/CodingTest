# AB
'''
S를 T로 만드는 것보다 T를 S로 만드는 것이 더 간단하다


'''
import sys
input=sys.stdin.readline

first_charlist=input().rstrip()

two_charlist=input().rstrip()

def check(string):
    if len(string)==len(first_charlist): #시작 문자열과 현재 문자열 길이가 같으면 stop하고 체크.
        if string==first_charlist: #같은 문자열이면,
                return True #만들 수 있는 것임. return True;
        return False #다르면 만들 수 없는 것임. return False;

    c1=string[-1] #맨 뒤에 있는 문자(A를 찾기 위함)
    c2=string[::-1][-1] #뒤집었을 때 맨 뒤에 있는 문자(B를 찾기 위함)

    # 두 케이스 모두 되는지 체크해봐야됨. (A, B에 관한 두가지)
    isOk1, isOk2=False, False #두 케이스 모두 불가능이라고 초기화
    
    if c1=='A': # A이면 그냥 하나 빼주고
        isOk1=check(string[:-1])

    if c2=='B': # B이면은 reverse를 하고 맨 뒤에 꺼를 뺀다
        isOk2=check(string[::-1][:-1])

    # 둘 중 하나라도 되면 만들 수 있는 것임.
    if isOk1 or isOk2:
        return True
    else:
        return False

if check(two_charlist):
    print(1)
else:
    print(0)


