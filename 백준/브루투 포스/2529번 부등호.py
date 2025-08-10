import sys
input=sys.stdin.readline
k=int(input())
n=9
equa_list=list(input().split())
visited=[False]*(n+1)
ans=[]

def check(x,y,equ):
    if equ=='<':
        if x>y:
            return False
    else:
        if x<y:
            return False
    return True

def search(idx,num):
    if idx==k+1:
        ans.append(num)
        return

    for i in range(n+1):
        if visited[i]==False:
            if idx==0 or check(num[idx-1],str(i),equa_list[idx-1]):
                visited[i]=True
                search(idx+1,num+str(i))
                visited[i]=False

search(0,'')

ans.sort()

print(ans[-1])
print(ans[0])
