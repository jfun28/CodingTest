import sys
input=sys.stdin.readline
count=0

n=int(input())
num=0

result=[]

def dfs(current,depth):
    if depth>10:
        return

    result.append(int(current)) # 현재까지 만든 수를 저장
    for i in range(int(current[-1])): # 현재 자릿수보다 더 작은 숫자만 붙일 수 있음
        dfs(current+str(i),depth+1)

for i in range(10):
    dfs(str(i),1)


result.sort()

if n>=len(result):
    print(-1)
else:
    print(result[n])
    

    





# def search(num):
#     global count
#     if count==n:
#         return num
    
#     for i in range(n):
#         search()




