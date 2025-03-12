<<<<<<< HEAD
s = input()
t = input()
 
def dfs(x):
    if len(x) == len(s):
        if x == s:
            print(1)
            exit()
        else:
            return
    if x[-1] == 'A':
        dfs(x[:-1])
    if x[0] == 'B':
        dfs(x[::-1][:-1])
    return
        
dfs(t)
print(0)
=======
import sys
input=sys.stdin.readline

S=input().strip()
T=input().strip()

def check(word):
    if len(S)==len(word):
        if S==word:
            return True
        else:
            return False
        
  
    if word[-1]=='A':
        if check(word[:-1]):
            return True
        
    if word[0]=="B":
        if check(word[::-1][:-1]):
            return True
    
    return False

answer=check(T)

if answer:
    print(1)
else:
    print(0)








# s = input()
# t = input()
 
# def dfs(x):
#     if len(x) == len(s):
#         if x == s:
#             print(1)
#             exit()
#         else:
#             return
#     if x[-1] == 'A':
#         dfs(x[:-1])
#     if x[0] == 'B':
#         dfs(x[::-1][:-1])
#     return
        
# dfs(t)
# print(0)









































>>>>>>> 9166241652410cf45b63048e8cda552f409c2e96
