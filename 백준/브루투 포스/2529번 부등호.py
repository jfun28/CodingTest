import sys
input=sys.stdin.readline

k=int(input())
visited=[False]*10
ans=[]
equa=list(input().split())

def check(x,y,oper):
    if oper=='<':
        if x>y:
            return False
    else:
        if x<y:
            return False
    return True

def dfs_find(idx,num):

    if idx==k+1:
        ans.append(num)
        return

    for i in range(10):
        if not visited[i]:
            if idx==0 or check(num[idx-1],str(i),equa[idx-1]):
                visited[i]=True
                dfs_find(idx+1,num+str(i))
                visited[i]=False

dfs_find(0,'')

ans.sort()

print(type(ans[-1]))
print(ans[0])


